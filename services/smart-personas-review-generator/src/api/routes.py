import logging
import time
from flask import request, jsonify
from .exceptions import MissingURLParameter, CustomServerError
from config import PERSONA_NAME, PARAGRAPH_LIMIT, ACCESSIBILITY_REPORTER_API
from data import report_loader
from data.personal_info_factory import PersonalInfoFactory
from review_generator import ReviewGenerator
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

RETRY_LIMIT = 3
RETRY_DELAY = 2  # in seconds
BACKOFF_FACTOR = 2


def init_routes(app):
    @app.route('/', methods=['GET'])
    def testing():
        time.sleep(2)
        url = request.args.get('url')
        return jsonify({"review": "hello world", "url": url})

    @app.route('/review', methods=['GET'])
    def generate_review():
        """Generate and return the review based on a given URL."""
        try:
            # Extract 'url' query parameter from the incoming request
            url = request.args.get('url')
            if not url:
                raise MissingURLParameter()

            for attempt in range(RETRY_LIMIT):
                try:
                    response = requests.get(ACCESSIBILITY_REPORTER_API + "/a11y-report", params={"url": url})
                    response.raise_for_status()

                    report_file = response.json()

                    generator = ReviewGenerator()
                    context = report_file['context']
                    violations = report_file['report']
                    persona = PersonalInfoFactory.get_persona(PERSONA_NAME)

                    response_text = generator.generate(context, violations, persona, PARAGRAPH_LIMIT)
                    return jsonify({"review": response_text})

                except requests.RequestException as req_err:
                    logger.warning("Attempt %s/%s - Failed to fetch data from the accessibility reporter due to %s",
                                   attempt + 1, RETRY_LIMIT, str(req_err))
                    if attempt + 1 == RETRY_LIMIT:
                        logger.exception("Failed to fetch data from the accessibility reporter after %s attempts", RETRY_LIMIT)
                        raise CustomServerError("Failed to fetch data from the accessibility reporter")

                    # Implement exponential backoff
                    sleep_time = RETRY_DELAY * (BACKOFF_FACTOR ** attempt)
                    time.sleep(sleep_time)

        except MissingURLParameter:
            logger.exception("URL parameter is missing in the request")
            raise CustomServerError("URL parameter is required.")

        except Exception as e:
            logger.exception("An unexpected error occurred")
            raise CustomServerError(str(e))

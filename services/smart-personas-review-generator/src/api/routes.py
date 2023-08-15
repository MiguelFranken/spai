import logging
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


def init_routes(app):

    @app.route('/', methods=['GET'])
    def test_connection():
        """Test route to verify API connection."""
        return jsonify({"review": "TEST"})

    @app.route('/review', methods=['GET'])
    def generate_review():
        """Generate and return the review based on a given URL."""
        try:
            # Extract 'url' query parameter from the incoming request
            url = request.args.get('url')
            if not url:
                raise MissingURLParameter()

            response = requests.get(ACCESSIBILITY_REPORTER_API + "/a11y-report", params={"url": url})
            response.raise_for_status()

            report_file = response.json()

            generator = ReviewGenerator()
            context = report_file['context']
            violations = report_file['report']
            persona = PersonalInfoFactory.get_persona(PERSONA_NAME)

            response_text = generator.generate(context, violations, persona, PARAGRAPH_LIMIT)
            return jsonify({"review": response_text})

        except requests.RequestException:
            logger.exception("Failed to fetch data from the accessibility reporter")
            raise CustomServerError("Failed to fetch data from the accessibility reporter")

        except MissingURLParameter:
            logger.exception("URL parameter is missing in the request")
            raise CustomServerError("URL parameter is required.")

        except Exception as e:
            logger.exception("An unexpected error occurred")
            raise CustomServerError(str(e))

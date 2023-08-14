from flask import Flask, request, jsonify, make_response
from config import PERSONA_NAME, PARAGRAPH_LIMIT, ACCESSIBILITY_REPORTER_API
from data import report_loader
from data.personal_info_factory import PersonalInfoFactory
from review_generator import ReviewGenerator
import requests


app = Flask(__name__)


# Custom Exception Classes
class MissingURLParameter(Exception):
    status_code = 400


class CustomServerError(Exception):
    status_code = 500


@app.errorhandler(MissingURLParameter)
def handle_missing_url_parameter(error):
    return make_response(jsonify({"error": "Missing URL query parameter"}), MissingURLParameter.status_code)


@app.errorhandler(CustomServerError)
def handle_custom_server_error(error):
    return make_response(jsonify({"error": str(error)}), CustomServerError.status_code)


@app.route('/review', methods=['GET'])
def generate_review():
    try:
        # Extract 'url' query parameter from the incoming request
        url = request.args.get('url')
        if not url:
            raise MissingURLParameter()

        # Fetch report data from accessibility-report.local
        response = requests.get(ACCESSIBILITY_REPORTER_API + "/a11y-report", params={"url": url})

        # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()

        # Extract the 'report' field from the JSON data
        report_file = response.json()

        # Initialize your review generator
        generator = ReviewGenerator()

        # Get the context and violations from the report
        context = report_file['context']
        violations = report_file['report']
        persona = PersonalInfoFactory.get_persona(PERSONA_NAME)

        # Generate the response text
        response_text = generator.generate(context, violations, persona, PARAGRAPH_LIMIT)

        # Return the response text in a JSON response
        return jsonify({"review": response_text})

    except requests.RequestException as e:  # Handling requests exceptions
        raise CustomServerError("Failed to fetch data from the accessibility reporter")

    except Exception as e:
        raise CustomServerError(str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

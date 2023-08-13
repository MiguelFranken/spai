# app.py
from flask import Flask, request, jsonify

from config import PERSONA_NAME, PARAGRAPH_LIMIT
from data import report_loader
from data.personal_info_factory import PersonalInfoFactory
from review_generator import ReviewGenerator

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test_connection():
    return jsonify({"review": "TEST"})


@app.route('/review', methods=['POST'])
def generate_review():
    try:
        # Get the JSON data from the request body
        data = request.get_json()

        # Check for the existence of the 'report' field in the JSON data
        if not data or 'report' not in data:
            return jsonify({"error": "Invalid or missing report data"}), 400

        # Extract the 'report' field from the JSON data
        report_file = data['report']

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

    except Exception as e:
        # Handle unexpected errors and return them in a JSON response
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)

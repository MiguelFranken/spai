from flask import jsonify, make_response
from .exceptions import MissingURLParameter, CustomServerError


def init_error_handlers(app):
    @app.errorhandler(MissingURLParameter)
    def handle_missing_url_parameter(error):
        """Handle errors related to missing URL parameters."""
        return make_response(jsonify({"error": "Missing URL query parameter"}), MissingURLParameter.status_code)

    @app.errorhandler(CustomServerError)
    def handle_custom_server_error(error):
        """Handle generic server errors."""
        return make_response(jsonify({"error": str(error)}), CustomServerError.status_code)

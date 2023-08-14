class MissingURLParameter(Exception):
    """Exception raised when the URL parameter is missing."""
    status_code = 400


class CustomServerError(Exception):
    """Exception raised for general server errors."""
    status_code = 500

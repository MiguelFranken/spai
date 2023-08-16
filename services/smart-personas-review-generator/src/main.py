from flask import Flask
from flask_cors import CORS
from api.routes import init_routes
from api.error_handlers import init_error_handlers

app = Flask(__name__)
CORS(app)

init_routes(app)
init_error_handlers(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)

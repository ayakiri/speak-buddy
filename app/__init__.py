from flask import Flask
from .handler import configure_routes


def create_app():
    """
    Creates and configures a Flask application instance.

    Returns:
    Flask: The configured Flask application.
    """
    app = Flask(__name__)

    # Configure the application routes
    configure_routes(app)

    return app

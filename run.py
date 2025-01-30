from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    """
    Entry point of the application.

    Starts the Flask server on host '0.0.0.0' (accessible from any network)
    and listens on port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
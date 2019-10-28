"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    # app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .dashboard import routes
        from .auth import routes

        # Register Blueprints
        app.register_blueprint(dashboard.routes.main_bp)
        app.register_blueprint(auth.routes.auth_bp)

        # Create Database Models
        db.create_all()

        return app
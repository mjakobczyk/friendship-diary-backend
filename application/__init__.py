"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt import JWT
# from security import authenticate, identity


db = SQLAlchemy()
jwt = None

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    print("Applying config")
    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    # jwt = JWT(app, authenticate, identity)

    with app.app_context():
        # Import parts of our application
        from .dashboard import routes
        from .auth import routes
        from .memories import routes
        from .friends import routes
        from .users import routes

        # Register Blueprints
        app.register_blueprint(dashboard.routes.main_bp)
        app.register_blueprint(auth.routes.auth_bp)
        app.register_blueprint(memories.routes.memories_bp)
        app.register_blueprint(friends.routes.friends_bp)
        app.register_blueprint(users.routes.users_bp)

        # Create Database Models
        db.create_all()

        return app

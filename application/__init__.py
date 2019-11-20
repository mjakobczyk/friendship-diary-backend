"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt import JWT
# from security import authenticate, identity
import logging


db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    print("Applying config")
    # Application Configuration
    app.config.from_object('config.Config')

    logging.info(app.secret_key)

    # Initialize Plugins
    db.init_app(app)

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

        logging.warning(jwt)

        return app

# This import has to be done after database variable definition
# in order to avoid circular import (and then variable db will
# not be visible)
# from application.auth.models import User

# def authenticate(username, password):
#     existing_user = User.query.filter(User.username == username and User.password == password).first()
#     if existing_user:
#         return existing_user

# def identity(payload):
#     user_id = payload['identity']
#     return UserModel.query.filter(User.id == user_id)

# jwt = JWT(app, authenticate, identity)
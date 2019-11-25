from os import environ
import logging

class Config:
    """Set Flask configuration vars from .env file."""

    # Logging
    logging.basicConfig(level=logging.DEBUG)

    # General
    TESTING = environ["TESTING"]
    FLASK_DEBUG = environ["FLASK_DEBUG"]

    # Database
    db_type=environ.get("DB_TYPE")
    user=environ.get("DB_USER")
    password=environ.get("DB_PASSWORD")
    hostname=environ.get("DB_HOSTNAME")
    port=environ.get("DB_PORT")
    db_name=environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(db_type, user, password, hostname, port, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    
    # JWT
    SECRET_KEY = environ["SECRET_KEY"]
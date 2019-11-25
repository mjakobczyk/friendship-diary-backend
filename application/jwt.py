from flask import current_app as app
from flask_jwt_extended import JWTManager

# JWT variable
jwt = JWTManager(app)
from application.auth.models import User
from flask import current_app as app
from flask_jwt import JWT

# Function for handling authentication in JWT
def authenticate(username, password):
    existing_user = User.query.filter(User.username == username and User.password == password).first()
    if existing_user:
        return existing_user

# Function for handling authorization in JWT
def identity(payload):
    user_id = payload['identity']
    return UserModel.query.filter(User.id == user_id)

# JWT variable
jwt = JWT(app, authenticate, identity)
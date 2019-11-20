from application.auth.models import User
from flask_jwt import JWT
from flask import current_app as app

def authenticate(username, password):
    existing_user = User.query.filter(User.username == username and User.password == password).first()
    if existing_user:
        return existing_user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id == user_id)

jwt = JWT(app, authenticate, identity)
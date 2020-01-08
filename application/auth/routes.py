from application.auth.models import User, user_registration_schema
from application import db
from application.jwt import jwt
from datetime import datetime, timedelta
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
import logging


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/login', methods=['GET', 'POST'])
def login():
    response = {}

    data = request.get_json()
    if not data:
        response["message"] = "No input data provided"
        return make_response(jsonify(response), 400)
    
    username = data.get('username')
    password = data.get('password')

    if username and password:
        existing_user = User.query.filter(User.username == username).first()

        if existing_user and existing_user.check_password(password):
            expires = timedelta(hours=1)
            response["token"] = create_access_token(identity = username, expires_delta=expires)
            return make_response(jsonify(response), 200)
        else:
            response["message"] = "Incorrect username or password"
            return make_response(jsonify(response), 401)    
    else:
        response["message"] = "Incorrect request parameters"
        return make_response(jsonify(data), 400)


@auth_bp.route('/api/register', methods=['POST'])
def register():
    response = {}

    data = request.get_json()
    if not data:
        response["message"] = "No input data provided"
        return make_response(jsonify(response), 400)

    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password = data.get('password')

    if username and firstname and password:
        try:
            existing_user = User.query.filter(User.username == username).first()
            
            if existing_user:
                response["message"] = "User with given name already exists"
                return make_response(jsonify(response), 422)
            else:
                expires = timedelta(hours=1)
                access_token = create_access_token(identity = username, expires_delta=expires)
                refresh_token = create_refresh_token(identity = username, expires_delta=expires)

                new_user = User(username=username,
                                firstname=firstname,
                                lastname=lastname,
                                createdon=datetime.now())
                
                new_user.set_password(password)

                db.session.add(new_user)
                db.session.commit()

                response = {
                    "message": "Created user: {}".format(new_user),
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }

                return make_response(jsonify(response), 201)
        except:
            response["message"] = "Error occured during request processing"
            return make_response(jsonify(response), 500)
    else:
        response["message"] = "Incorrect request parameters"
        return make_response(jsonify(response), 400)

@auth_bp.route('/api/protected', methods=['GET'])
@jwt_required
def protected():
    response = {
        "message": "Successful authorization",
        "username": get_jwt_identity()
    }
    return make_response(jsonify(response))

from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from application.auth.models import User, user_registration_schema
from application import db
from application.jwt import jwt
from datetime import datetime
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity)
import logging


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/login', methods=['GET'])
def login():
    response = {
        "message": "",
    }

    if request.method == 'GET':
        response["message"] = "Mocked GET /api/login"
        return make_response(jsonify(response), 200)
    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if username and password:
            existing_user = User.query.filter(User.username == username and User.password == password).first()
            if existing_user:
                response["message"] = "User credentials OK!"
                return make_response(jsonify(data), 200)
            else:
                response["message"] = "User not found!"
                return make_response(jsonify(data), 404)    
        else:
            response["message"] = "Incorrect parameters passed for creating new user"
            return make_response(jsonify(data), 400)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)


@auth_bp.route('/api/register', methods=['GET', 'POST'])
def register():
    response = {
        "message": "",
    }

    if request.method == 'GET':
        response["message"] = "Mocked GET /api/register"
        return make_response(jsonify(response), 200)
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            response["message"] = "No input data provided"
            return make_response(jsonify(response), 400)
    
        username = data.get('username')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        password = data.get('password')

        if username and firstname and password:
            # try:
                existing_user = User.query.filter(User.username == username).first()
                
                if existing_user:
                    response["message"] = "User with given data already exists!"
                    return make_response(jsonify(response), 422)
                else:
                    # TODO: add password hashing
                    access_token = create_access_token(identity = username)
                    refresh_token = create_refresh_token(identity = username)

                    new_user = User(username=username,
                                    firstname=firstname,
                                    lastname=lastname,
                                    password=password,
                                    createdon=datetime.now())
                    db.session.add(new_user)
                    db.session.commit()

                    response = {
                        "message": "Created user: {}".format(new_user),
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    }

                    return make_response(jsonify(response), 201)
        else:
            response["message"] = "Incorrect parameters passed for creating new user"
            return make_response(jsonify(response), 400)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@auth_bp.route('/api/protected', methods=['GET'])
@jwt_required
def protected():
    response = {
        "message": "Successful authorization!",
        "username": get_jwt_identity()
    }
    return make_response(jsonify(response))

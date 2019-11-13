from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from application.auth.models import User
from application import db
from datetime import datetime
import logging


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/login', methods=['GET'])
def login():
    response = {
        "message": "",
    }

    # POST
    if request.method == 'POST':
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

    # GET
    response["message"]="Mocked GET /api/login"
    return make_response(jsonify(data), 200)

@auth_bp.route('/api/register', methods=['GET', 'POST'])
def register():
    resp = {
        "message": "",
    }

    data = request.get_json()
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password = data.get('password')

    # POST
    if request.method == 'POST':
        if username and firstname and password:
            existing_user = User.query.filter(User.username == username).first()
            if existing_user:
                resp["message"] = "User with given data already exists!"
                return make_response(jsonify(resp), 422)
            else:
                # TODO: add password hashing
                new_user = User(username=username,
                                firstname=firstname,
                                lastname=lastname,
                                password=password,
                                createdon=datetime.now())  # Create an instance of the User class
                db.session.add(new_user)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                resp["message"] = "Created user: {}".format(new_user)
                
                return make_response(jsonify(resp), 201)
        else:
            resp["message"] = "Incorrect parameters passed for creating new user"
            return make_response(jsonify(resp), 400)

    # GET
    resp["message"]="Mocked GET /api/register"
    return make_response(jsonify(resp), 200)

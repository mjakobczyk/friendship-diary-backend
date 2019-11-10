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
    data = {
        "message": "",
    }

    # POST
    if request.method == 'POST':
        data["message"]="Mocked POST /api/login"
        return make_response(jsonify(data), 200)

    # GET
    data["message"]="Mocked GET /api/login"
    return make_response(jsonify(data), 200)

@auth_bp.route('/api/register', methods=['GET', 'POST'])
def register():
    data = {
        "message": "",
    }

    username = "username" # username = request.args.get('username')
    firstname = "firstname" # firstname = request.args.get('firstname')
    lastname = "lastname" # lastname = request.args.get('lastname')
    password = "password" # password =  request.args.get('password')
    email = "email" # email = request.args.get('email')

    # POST
    if request.method == 'POST':
        if username and firstname and password:
            existing_user = User.query.filter(User.username == username or User.email == email).first()
            if existing_user:
                data["message"] = "User with given data already exists!"
                return make_response(jsonify(data), 400)
            else:
                new_user = User(username=username,
                                firstname=firstname,
                                lastname=lastname,
                                email=email,
                                createdon=datetime.now())  # Create an instance of the User class
                db.session.add(new_user)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                data["message"] = "created user: {}".format(new_user)
                
                return make_response(jsonify(data), 200)
        else:
            data["message"] = "Incorrect parameters passed for creating new user"
            return make_response(jsonify(data), 400)

    # GET
    data["message"]="Mocked GET /api/register"
    return make_response(jsonify(data), 200)

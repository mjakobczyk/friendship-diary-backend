from application import db
from application.auth.models import User, user_schema, users_schema
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging
import json

# Blueprint Configuration
users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/api/users', methods=['GET'])
@jwt_required
def getAllUsers():
    response = {}

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()
    users = User.query.filter(User.id != user.id)
    
    response["items"] = users_schema.dump(users)
    return make_response(jsonify(response), 200)
        
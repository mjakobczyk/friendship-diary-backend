from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from application import db
from application.auth.models import User
from application.auth.models import user_schema
from application.auth.models import users_schema
import logging
import json

# Blueprint Configuration
users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/api/users', methods=['GET'])
def getAllUsers():
    response = {
        "items": ""
    }

    if request.method == 'GET':
        users = User.query.all()
        response["items"] = users_schema.dump(users)
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)
        
from application import db
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required
import logging

# Blueprint Configuration
friends_bp = Blueprint('friends_bp', __name__)


@friends_bp.route('/api/friends', methods=['GET'])
@jwt_required
def getAllFriends():
    response = {}

    if request.method == 'GET':
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()

        # TODO
        response["items"] = "Mocked GET /api/friends response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)


# TODO: change id to query parameter
@friends_bp.route('/api/friend/id', methods=['DELETE'])
@jwt_required
def removeFriend():
    response = {
        "message": "",
    }

    if request.method == 'DELETE':
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()

        # TODO
        response["message"] = "Mocked DELETE /api/friend/id response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)
from application import db
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from application.auth.models import User, user_schema, users_schema
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
        friends = user.friends
        # logging.info(friends)
        logging.info(users_schema.dump(friends))

        # response["items"] = users_schema.dump(friends)
        # TODO
        response["message"] = "Mocked GET /api/friends response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@friends_bp.route('/api/friend/<name>', methods=['POST'])
@jwt_required
def addFriend(name):
    response = { }

    if request.method == 'POST':
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()
        friend = User.query.filter(User.username == name).first()

        if friend == None:
            response["message"] = "Friend with given id was not found"
            return make_response(jsonify(response), 404)

        if user == friend:
            response["message"] = "You can not friend yourself"
            return make_response(jsonify(response), 400)  

        # TODO: add validation if user has been already added to friends
        user.befriend(friend)

        db.session.add(user)
        db.session.commit()

        response["message"] = "Successfully added new friend"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)


# TODO: change id to query parameter
@friends_bp.route('/api/friend/name', methods=['DELETE'])
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
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from application import db
import logging

# Blueprint Configuration
memories_bp = Blueprint('memories_bp', __name__)


@memories_bp.route('/api/memory', methods=['POST'])
def createNewMemmory():
    response = {
        "message": "",
    }

    if request.method == 'POST':
        # TODO
        response["message"] = "Mocked POST /api/memory response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@memories_bp.route('/api/memories', methods=['GET'])
def getAllMemories():
    response = {
        "message": "",
    }

    if request.method == 'GET':
        # TODO
        response["message"] = "Mocked GET /api/memories response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@memories_bp.route('/api/memories/draft', methods=['GET', 'POST'])
def getOrAddMemoryDraft():
    response = {
        "message": "",
    }

    if request.method == 'GET':
        # TODO
        response["message"] = "Mocked GET /api/memories/draft response"
        return make_response(jsonify(response), 200)
    elif request.method == 'POST':
        # TODO
        response["message"] = "Mocked POST /api/memories/draft response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

# TODO: add draft id as a query parameter
@memories_bp.route('/api/memories/draft/draft_id', methods=['PUT'])
def updateMemoryDraft():
    response = {
        "message": "",
    }

    if request.method == 'PUT':
        # TODO
        response["message"] = "Mocked PUT /api/memories/draft/<draft_id> response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)
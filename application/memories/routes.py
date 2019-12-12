from application import db
from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from application.auth.models import User
from .models import Memory
import logging

# Blueprint Configuration
memories_bp = Blueprint('memories_bp', __name__)


@memories_bp.route('/api/memory', methods=['POST'])
@jwt_required
def createNewMemmory():
    response = {}

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            response["message"] = "No input data provided"
            return make_response(jsonify(response), 400)

        try:
            from .models import memory_schema
            
            memory = memory_schema.load(data)

            if memory.title and memory.description and memory.image:
                username = get_jwt_identity()
                user = User.query.filter(User.username == username).first()

                memory.user_id=user.id

                db.session.add(memory)
                db.session.commit()

                response["memory"] = memory_schema.dump(memory)
                return make_response(jsonify(response), 200)
            else:
                response["message"] = "Incorrect request parameters"
                return make_response(jsonify(data), 400)
        except:
            response["message"] = "Error occured during request processing"
            return make_response(jsonify(response), 500)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@memories_bp.route('/api/memories', methods=['GET'])
@jwt_required
def getAllMemories():
    response = {
        "items": "",
    }

    if request.method == 'GET':
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()
        userMemories = Memory.query.filter(Memory.user_id == user.id).all()

        from .models import memories_schema

        response["items"] = memories_schema.dump(userMemories)
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 405)

@memories_bp.route('/api/memories/draft', methods=['GET', 'POST'])
@jwt_required
def getOrAddMemoryDraft():
    response = {}

    if request.method == 'GET':
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()

        from .models import MemoryDraft
        from .models import memories_drafts_schema

        userMemoriesDrafts = MemoryDraft.query.filter(MemoryDraft.user_id == user.id).all()

        response["items"] = memories_drafts_schema.dump(userMemoriesDrafts)
        return make_response(jsonify(response), 200)
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            response["message"] = "No input data provided"
            return make_response(jsonify(response), 400)

        try:
            from .models import memory_draft_schema
            
            memory_draft = memory_draft_schema.load(data)

            username = get_jwt_identity()
            user = User.query.filter(User.username == username).first()

            memory_draft.user_id=user.id

            db.session.add(memory_draft)
            db.session.commit()

            response["memory_draft"] = memory_draft_schema.dump(memory_draft)
            return make_response(jsonify(response), 200)

            # response["message"] = "Ok"
            # return make_response(jsonify(response), 200)
        except:
            response["message"] = "Error occured during request processing"
            return make_response(jsonify(response), 500)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

@memories_bp.route('/api/memories/draft/<int:draft_id>', methods=['PUT'])
@jwt_required
def updateMemoryDraft(draft_id):
    response = {}

    if request.method == 'PUT':
        if request.view_args:
        
            # TODO: process draft_id, look for draft, update
            # accordingly
            response["message"] = "Mocked PUT /api/memories/draft/<draft_id> response"
            return make_response(jsonify(response), 200)
        else:
            response["message"] = "No query parameters received"
            return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)
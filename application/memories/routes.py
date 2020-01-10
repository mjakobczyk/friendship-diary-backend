from application import db
from datetime import datetime
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

@memories_bp.route('/api/memories', methods=['GET'])
@jwt_required
def getAllMemories():
    response = {}

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()
    
    userMemories = Memory.query.filter(Memory.user_id == user.id).order_by(Memory.id.asc()).all()

    from .models import memories_schema

    response["items"] = memories_schema.dump(userMemories)
    return make_response(jsonify(response), 200)

@memories_bp.route('/api/memory', methods=['POST'])
@jwt_required
def addMemory():
    response = {}

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
            memory.uploaded = datetime.now()

            # Validate friends list
            existing_friends = []
            
            for friend_name in memory.friends:
                friend = User.query.filter(User.username == friend_name).first()
                if user.is_friend(friend):
                    existing_friends.append(friend_name)

            memory.friends = existing_friends

            db.session.add(memory)
            db.session.commit()

            response["memory"] = memory_schema.dump(memory)
            return make_response(jsonify(response), 200)
        else:
            response["message"] = "Incorrect request parameters"
            return make_response(jsonify(data), 400)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)

@memories_bp.route('/api/memories/<int:memory_id>', methods=['PUT'])
@jwt_required
def updateMemory(memory_id):
    response = {}

    if not request.view_args:
        response["message"] = "No query parameters received"
        return make_response(jsonify(response), 200)

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()

    from .models import Memory

    memory = Memory.query.filter(Memory.id == memory_id and Memory.id == user.id).first()

    if memory == None:
        response["message"] = "Memory with current ID was not found"
        return make_response(jsonify(response), 404)

    data = request.get_json()
    if not data:
        response["message"] = "No input data provided"
        return make_response(jsonify(response), 400)

    try:
        from .models import memory_schema

        loaded_memory = memory_schema.load(data)
        loaded_memory.id = memory.id
        loaded_memory.uploaded = datetime.now()

        db.session.merge(loaded_memory)
        db.session.commit()

        response["memory"] = memory_schema.dump(loaded_memory)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)

@memories_bp.route('/api/memories/<int:memory_id>', methods=['DELETE'])
@jwt_required
def deleteMemory(memory_id):
    response = {}

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()

    from .models import Memory

    memory = Memory.query.filter(Memory.id == memory_id and Memory.id == user.id).first()

    if memory == None:
        response["message"] = "Memory with current ID was not found"
        return make_response(jsonify(response), 404)

    try:
        db.session.delete(memory)
        db.session.commit()

        from .models import memory_schema

        response["memory"] = memory_schema.dump(memory)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)

@memories_bp.route('/api/memories/drafts', methods=['GET'])
@jwt_required
def getAllMemoryDrafts():
    response = {}

    try:
        username = get_jwt_identity()
        user = User.query.filter(User.username == username).first()

        from .models import MemoryDraft
        from .models import memories_drafts_schema

        userMemoriesDrafts = MemoryDraft.query.filter(MemoryDraft.user_id == user.id).order_by(MemoryDraft.id.asc()).all()

        response["items"] = memories_drafts_schema.dump(userMemoriesDrafts)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)

@memories_bp.route('/api/memories/draft', methods=['POST'])
@jwt_required
def addMemoryDraft():
    response = {}

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

        # Validate friends list
        existing_friends = []
        
        for friend_name in memory_draft.friends:
            friend = User.query.filter(User.username == friend_name).first()
            if user.is_friend(friend):
                existing_friends.append(friend_name)
                
        memory_draft.friends = existing_friends

        db.session.add(memory_draft)
        db.session.commit()

        response["memory_draft"] = memory_draft_schema.dump(memory_draft)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)

@memories_bp.route('/api/memories/draft/<int:draft_id>', methods=['PUT'])
@jwt_required
def updateMemoryDraft(draft_id):
    response = {}

    if not request.view_args:
        response["message"] = "No query parameters received"
        return make_response(jsonify(response), 200)

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()

    from .models import MemoryDraft

    memory_draft = MemoryDraft.query.filter(MemoryDraft.id == draft_id and MemoryDraft.id == user.id).first()

    if memory_draft == None:
        response["message"] = "MemoryDraft with current ID was not found"
        return make_response(jsonify(response), 404)

    data = request.get_json()
    if not data:
        response["message"] = "No input data provided"
        return make_response(jsonify(response), 400)

    try:
        from .models import memory_draft_schema

        loaded_memory_draft = memory_draft_schema.load(data)
        loaded_memory_draft.id = memory_draft.id

        db.session.merge(loaded_memory_draft)
        db.session.commit()

        response["memory_draft"] = memory_draft_schema.dump(loaded_memory_draft)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)



@memories_bp.route('/api/memories/draft/<int:draft_id>', methods=['DELETE'])
@jwt_required
def deleteMemoryDraft(draft_id):
    response = {}

    username = get_jwt_identity()
    user = User.query.filter(User.username == username).first()

    from .models import MemoryDraft

    memory_draft = MemoryDraft.query.filter(MemoryDraft.id == draft_id and MemoryDraft.id == user.id).first()

    if memory_draft == None:
        response["message"] = "MemoryDraft with current ID was not found"
        return make_response(jsonify(response), 404)

    try:
        db.session.delete(memory_draft)
        db.session.commit()

        from .models import memory_draft_schema

        response["memory_draft"] = memory_draft_schema.dump(memory_draft)
        return make_response(jsonify(response), 200)
    except Exception as ex:
        response["message"] = "Error occured during request processing"
        logging.error(ex)
        return make_response(jsonify(response), 500)
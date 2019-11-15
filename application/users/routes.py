from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response
from application import db
from application.auth.models import User
import logging
import json

# Blueprint Configuration
users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/api/users', methods=['GET'])
def getAllUsers():
    response = {
        "message": "",
        "users": ""
    }

    if request.method == 'GET':
        # TODO: add dict to users
        # json_data = json.dumps([ob.to_dict() for ob in users])
        # json_data = json.dumps(users.__dict__ , default=lambda o: o.__dict__, indent=4)
        # json_data = json.dumps(users)

        # json_data = json.dumps(users, cls=new_alchemy_encoder(), check_circular=False)

        # logging.info("Users: {}".format(users))
        
        response["message"] = "Mocked GET /api/friends response"
        return make_response(jsonify(response), 200)
    else:
        response["message"] = "Method not allowed"
        return make_response(jsonify(response), 405)

from sqlalchemy.ext.declarative import DeclarativeMeta

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
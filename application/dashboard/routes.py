from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
from flask_login import login_required
from flask import request, jsonify, make_response

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', methods=['GET'])
def dashboard():
    data = {
        "message": "Welcome to Friendship Diary application!",
        "version": "1.0"
    }

    return make_response(jsonify(data), 200)

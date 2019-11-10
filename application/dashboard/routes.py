from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
from flask_login import login_required
from flask import request, jsonify, make_response
from os import environ
from application.auth.models import User
import logging

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', methods=['GET'])
def dashboard():
    data = {
        "message": "Welcome to Friendship Diary application!",
        "users": "",
        "version": "1.0"
    }

    users = User.query.all()

    # data["users"]=users
    logging.info("Users: {}".format(users))

    return make_response(jsonify(data), 200)

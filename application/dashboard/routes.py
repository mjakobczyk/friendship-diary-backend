from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
from flask_login import login_required

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', methods=['GET'])
def dashboard():
    return "Application dashboard"
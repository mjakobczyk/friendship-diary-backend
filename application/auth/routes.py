from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request

# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/login', methods=['GET'])
def login():
    # POST
    if request.method == 'POST':
        return "Mocked /api/login POST"

    # GET
    return "Mocked /login GET"

@auth_bp.route('/api/register', methods=['GET', 'POST'])
def register():
    # POST
    if request.method == 'POST':
        username = request.args.get('user')
        email = request.args.get('email')
        if username and email:
            new_user = User(username=username,
                            email=email,
                            created=dt.now(),
                            bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                            admin=False)  # Create an instance of the User class
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
            return "Added user /api/register POST"
        else:
            return "Incorrect parameters /api/register POST"

    # GET
    return "Mocked /api/register GET"
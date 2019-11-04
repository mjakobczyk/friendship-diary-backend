from flask import Blueprint
from flask_login import current_user
from flask import current_app as app
from flask import request, jsonify, make_response


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/api/login', methods=['GET'])
def login():
    data = {
        "message": "",
    }

    # POST
    if request.method == 'POST':
        data["message"]="Mocked POST /api/login"
        return make_response(jsonify(data), 200)

    # GET
    data["message"]="Mocked GET /api/login"
    return make_response(jsonify(data), 200)

@auth_bp.route('/api/register', methods=['GET', 'POST'])
def register():
    data = {
        "message": "",
    }

    # # POST
    if request.method == 'POST':
        data["message"]="Mocked POST /api/register"

        new_user = User(username="username",
                        email="email",
                        created=dt.now(),
                        bio="bio",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        
        return make_response(jsonify(data), 200)

        # username = request.args.get('user')
        # email = request.args.get('email')
        # if username and email:
        #     new_user = User(username=username,
        #                     email=email,
        #                     created=dt.now(),
        #                     bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
        #                     admin=False)  # Create an instance of the User class
        #     db.session.add(new_user)  # Adds new User record to database
        #     db.session.commit()  # Commits all changes
        #     return "Added user /api/register POST"
        # else:
        #     return "Incorrect parameters /api/register POST"

    # GET
    data["message"]="Mocked GET /api/register"
    return make_response(jsonify(data), 200)

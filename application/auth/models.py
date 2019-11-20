from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Model for user accounts."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String,
                     nullable=False,
                     unique=False)            
    firstname = db.Column(db.String,
                     nullable=False,
                     unique=False)
    lastname = db.Column(db.String,
                     nullable=True,
                     unique=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    createdon = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {} {} {} >'.format(self.username,
                                          self.firstname,
                                          self.lastname)

    def to_dict(self):
        return self.__dict__

from marshmallow_sqlalchemy import ModelSchema
from flask import current_app as app

class UserSchema(ModelSchema):
    class Meta:
        model = User
        # Fields to expose
        fields = ("username", "firstname", "lastname")

user_schema = UserSchema(session=db.session)
users_schema = UserSchema(session=db.session, many=True)

class UserRegistrationSchema(ModelSchema):
    class Meta:
        model = User
        # Fields to expose
        fields = ("username", "firstname", "lastname", "password")

user_registration_schema = UserRegistrationSchema(session=db.session)
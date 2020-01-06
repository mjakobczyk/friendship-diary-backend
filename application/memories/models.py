from application import db

class Localization(db.Model):
    """Model for localization."""

    __tablename__ = "localizations"

    # Columns
    id = db.Column(db.Integer,
                   primary_key=True)
    latitude = db.Column(db.String,
                    nullable=False,
                    unique=False)  
    longitude = db.Column(db.String,
                    nullable=False,
                    unique=False)
    memory_id = db.Column(db.Integer,
                    db.ForeignKey('memories.id'),
                    nullable=True) # TODO: add unique false
    memory_draft_id = db.Column(db.Integer,
                    db.ForeignKey('memoriesDrafts.id'),
                    nullable=True) # TODO: add unique false 

    def __repr__(self):
        return '<Localization: latitude = {}, longitude = {}>'.format(self.latitude,
                                          self.longitude)

from marshmallow_sqlalchemy import ModelSchema

class LocalizationSchema(ModelSchema):
    class Meta:
        model = Localization
        fields = ("latitude", "longitude")

localization_schema = LocalizationSchema(session=db.session)

class Memory(db.Model):
    """Model for memory."""

    __tablename__ = "memories"
    
    # Columns
    id = db.Column(db.Integer,
                primary_key=True)
    title = db.Column(db.String,
                nullable=False,
                unique=False)
    description = db.Column(db.String,
                nullable=False,
                unique=False)
    image = db.Column(db.String,
                nullable=False,
                unique=False)
    user_id = db.Column(db.Integer,
                db.ForeignKey('users.id'))
    friends = db.Column(db.ARRAY(db.String))

    # Relations
    localization = db.relationship("Localization",
                backref="memories",
                uselist=False)

    def __repr__(self):
        return '<Memory: {}>'.format(self.title)


from marshmallow_sqlalchemy.fields import Nested

class MemorySchema(ModelSchema):

    localization = Nested(LocalizationSchema, many=False)

    class Meta:
        model = Memory
        # Restrict fields if necessary
        # fields = ("...")

memory_schema = MemorySchema(session=db.session)
memories_schema = MemorySchema(session=db.session, many=True)

class MemoryDraft(db.Model):
    """Model for MemoryDraft."""

    __tablename__ = "memoriesDrafts"

    # Columns
    id = db.Column(db.Integer,
                primary_key=True)
    title = db.Column(db.String,
                nullable=False,
                unique=False)
    description = db.Column(db.String,
                nullable=False,
                unique=False)
    image = db.Column(db.String,
                nullable=False,
                unique=False)
    user_id = db.Column(db.Integer,
                db.ForeignKey('users.id'))
    friends = db.Column(db.ARRAY(db.String))

    # Relations
    localization = db.relationship("Localization",
                backref="memoriesDrafts",
                uselist=False)

    def __repr__(self):
        return '<Memory Draft: {}>'.format(self.title)

class MemoryDraftSchema(ModelSchema):

    localization = Nested(LocalizationSchema, many=False)

    class Meta:
        model = MemoryDraft
        # Restrict fields if necessary
        # fields = ("...")

memory_draft_schema = MemoryDraftSchema(session=db.session)
memories_drafts_schema = MemoryDraftSchema(session=db.session, many=True)


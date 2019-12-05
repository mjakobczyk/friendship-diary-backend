from application import db

class Localization(db.Model):
    """Model for localization."""

    __tablename__ = 'localizations'

    id = db.Column(db.Integer,
                   primary_key=True)
    latitude = db.Column(db.String,
                    nullable=False,
                    unique=False)  

    longitude = db.Column(db.String,
                    nullable=False,
                    unique=False)


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

    __tablename__ = 'memories'

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
    image = db.Column(db.String,
                    nullable=False,
                    unique=False)
                
    from sqlalchemy.orm import relationship

    # Relations
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    localization = relationship("Localization")

    def __repr__(self):
        return '<Memory: {}>'.format(self.title)


from sqlalchemy.orm import relationship

Localization.memory = relationship("Memory")

# Localization.memory = relationship("Memory", order_by = Memory.id, back_populates="localizations")

class MemorySchema(ModelSchema):
    class Meta:
        model = Memory
        # Restrict fields if necessary
        # fields = ("...")

memory_schema = MemorySchema(session=db.session)
memories_schema = MemorySchema(session=db.session, many=True)
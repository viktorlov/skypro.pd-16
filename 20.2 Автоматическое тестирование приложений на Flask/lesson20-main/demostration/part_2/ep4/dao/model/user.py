from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    age = fields.Int()

from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from setup_db import db


class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String)
    books = relationship('Book')


class AuthorSchema(Schema):
    author_id = fields.Int(dump_only=True)
    author_name = fields.Str()
    books = fields.Str()

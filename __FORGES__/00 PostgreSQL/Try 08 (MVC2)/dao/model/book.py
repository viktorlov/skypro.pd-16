from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from setup_db import db


class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
    author_name = relationship('Author', overlaps='books')


class BookSchema(Schema):
    book_id = fields.Int(dump_only=True)
    book_name = fields.Str()
    author_id = fields.Int()
    author_name = fields.Pluck('AuthorSchema', 'author_name')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:sql@localhost:5432/lesson15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)


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


class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String)
    books = relationship('Book')


class AuthorSchema(Schema):
    author_id = fields.Int(dump_only=True)
    author_name = fields.Str()
    books = fields.Str()


book_schema = BookSchema()
books_schema = BookSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


@app.route('/books/')
def get_all_books():
    books_list = Book.query.all()
    return books_schema.dump(books_list)


@app.route('/books/<int:bid>/')
def get_book_by_id(bid):
    book = Book.query.get(bid)
    if book is None:
        return f"Book with id {bid} not found"
    return book_schema.dump(book)


@app.route('/authors/')
def get_all_authors():
    authors_list = Author.query.all()
    return authors_schema.dump(authors_list)


@app.route('/authors/<int:aid>/')
def get_author_by_id(aid):
    author = Author.query.get(aid)
    if author is None:
        return f"Author with id {aid} not found"
    return author_schema.dump(author)


if __name__ == '__main__':
    app.run(debug=True)

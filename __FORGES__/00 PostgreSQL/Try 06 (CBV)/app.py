from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:sql@localhost:5432/lesson15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

api = Api(app)

book_ns = api.namespace('books')
author_ns = api.namespace('authors')


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


# noinspection PyArgumentList,PyMethodMayBeStatic
@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books_list = db.session.query(Book).all()
        return books_schema.dump(books_list), 200

    def post(self):
        new_book_data = request.json
        new_book = Book(**new_book_data)
        try:
            with db.session.begin():
                db.session.add(new_book)
            return "", 201
        except IntegrityError:
            new_author = Author(author_id=new_book.book_id,
                                author_name='unknown author for book' + str(new_book.book_id),
                                books=[new_book])
            try:
                with db.session.begin():
                    db.session.add(new_author)
                    db.session.add(new_book)
                return "", 201
            except Exception as e:
                return f'{e}', 404


# noinspection PyMethodMayBeStatic,PyArgumentList
@book_ns.route('/<int:bid>/')
class BookView(Resource):
    def get(self, bid):
        try:
            book = db.session.query(Book).filter(Book.book_id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return f'{e}', 404

    def put(self, bid):
        updated_book = db.session.query(Book).filter(Book.book_id == bid).update(request.json)
        if not updated_book:
            return 'no such book', 400
        db.session.commit()
        return "", 204

    def patch(self, bid):
        updated_book = db.session.query(Book).filter(Book.book_id == bid).update(request.json)
        if not updated_book:
            return 'no such book', 400
        db.session.commit()
        return "", 204

    def delete(self, bid):
        deleted_book = db.session.query(Book).get(bid)
        try:
            db.session.delete(deleted_book)
            db.session.commit()
            return "", 204
        except Exception as e:
            return f'{e}', 404


# noinspection PyMethodMayBeStatic
@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        authors_list = db.session.query(Author).all()
        return authors_schema.dump(authors_list), 200


# noinspection PyMethodMayBeStatic
@author_ns.route('/<int:aid>/')
class AuthorView(Resource):
    def get(self, aid):
        try:
            author = db.session.query(Author).filter(Author.author_id == aid).one()
            return author_schema.dump(author), 200
        except Exception as e:
            return f'{e}', 404


if __name__ == '__main__':
    app.run(host='127.0.0.6', port=10006, debug=True)

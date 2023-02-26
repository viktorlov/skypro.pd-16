import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:sql@localhost:5432/lesson15'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String)
    books = relationship('Book')


class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
    author_name = relationship('Author', overlaps='books')


@app.route('/books/first/')
def get_first_book():
    first_book = Book.query.first()
    return json.dumps({"book_id": first_book.book_id,
                       "book_name": first_book.book_name,
                       "author_id": first_book.author_id})


@app.route('/books/count/')
def get_count_books():
    books_count = Book.query.count()
    return json.dumps(books_count)


@app.route('/books/')
def get_all_books():
    books_list = Book.query.all()
    books_response = []
    for book in books_list:
        books_response.append({"book_id": book.book_id,
                               "book_name": book.book_name,
                               "author_id": book.author_id})
    return json.dumps(books_response)


@app.route('/books/<int:bid>/')
def get_book_by_id(bid):
    book = Book.query.get(bid)
    if book is None:
        return f"Book with id {bid} not found"
    return json.dumps({"book_id": book.book_id,
                       "book_name": book.book_name,
                       "author_id": book.author_id})


if __name__ == '__main__':
    app.run(debug=True)

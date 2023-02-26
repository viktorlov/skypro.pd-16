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


db.drop_all()
db.create_all()

author_id_1 = Author(author_id=1, author_name='Терри Пратчетт')
author_id_2 = Author(author_id=2, author_name='Джон Фаулз')
author_id_3 = Author(author_id=3, author_name='М.А. Булгаков')

new_authors = [author_id_1, author_id_2, author_id_3]

book_id_1 = Book(book_id=1, book_name='Изумительный Морис и его ученые грызуны', author_id=1)
book_id_2 = Book(book_id=2, book_name='Мор, ученик Смерти', author_id=1)
book_id_3 = Book(book_id=3, book_name='Стража! Стража!', author_id=1)
book_id_4 = Book(book_id=4, book_name='Коллекционер', author_id=2)
book_id_5 = Book(book_id=5, book_name='Женщина французского лейтенанта', author_id=2)
book_id_6 = Book(book_id=6, book_name='Волхв', author_id=2)
book_id_7 = Book(book_id=7, book_name='Мастер и Маргарита', author_id=3)

new_books = [book_id_1, book_id_2, book_id_3, book_id_4, book_id_5, book_id_6, book_id_7]

db.session.add_all(new_authors)
db.session.add_all(new_books)
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)

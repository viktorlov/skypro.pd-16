from flask import request
from flask_restx import Resource, Namespace
from models import Book
from setup_db import db

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books = Book.query.all()
        result = []
        for book in books:
            temp = book.__dict__
            del temp['_sa_instance_state']
            result.append(temp)
        return result, 200

    def post(self):
        json_request = request.json
        temp = Book(**json_request)
        try:
            db.session.add(temp)
            db.session.commit()
            return "", 201
        except Exception as e:
            return {'message': str(e)}, 500



@book_ns.route('/<int:bid>/')
class BookView(Resource):
    def get(self, bid):
        book = Book.query.get(bid)
        try:
            result = book.__dict__
            del result['_sa_instance_state']
            return result, 200
        except Exception as e:
            return {'message': str(e)}, 500


    def put(self, bid):
        updated_book = db.session.query(Book).filter(Book.id == bid).update(request.json)
        if not updated_book:
            return f"Книга с индексом {bid} не найдена.", 400
        db.session.commit()
        return "", 204

    def delete(self, bid):
        deleted_book = Book.query.get(bid)
        try:
            db.session.delete(deleted_book)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500

from flask import request
from flask_restx import Resource, Namespace

from dao.model.book import BookSchema
from implemented import book_service

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        books = book_service.get_all()

        def _print_v1():
            print('VIEWS: get_all')
            print(f'VIEWS OUTPUT {books = }')
            print(f'VIEWS OUTPUT {type(books) = }')

        _print_v1()
        return BookSchema(many=True).dump(books), 200

    def post(self):
        book_service.create(request.json)
        return "", 201


@book_ns.route('/<int:bid>/')
class BookView(Resource):
    def get(self, bid):
        book = book_service.get_one(bid)

        def _print_v2():
            print('VIEWS: get_one')
            print(f'VIEWS INPUT {bid = }')
            print(f'VIEWS INPUT {type(bid) = }')
            print(f'VIEWS OUTPUT {book = }')
            print(f'VIEWS OUTPUT {type(book) = }')

        _print_v2()

        return BookSchema().dump(book), 200

    def put(self, bid):
        reg_json = request.json
        reg_json["id"] = bid
        book_service.update(reg_json)
        return "", 204

    def patch(self, bid):
        pass

    def delete(self, bid):
        book_service.delete(bid)
        return "", 204

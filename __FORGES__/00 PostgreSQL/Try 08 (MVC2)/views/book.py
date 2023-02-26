from flask import request
from flask_restx import Resource, Namespace

from dao.model.book import BookSchema
from implemented import book_service

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        """
        GET ALL.
        @return: All books from the database.
        """
        return BookSchema(many=True).dump(book_service.get_all()), 200

    def post(self):
        """
        POST.
        @return: 201 Created.
        """
        book_service.create(request.json)
        return "method:post", 201


@book_ns.route('/<int:bid>/')
class BookView(Resource):
    def get(self, bid):
        """
        GET ONE.
        @param bid: Book ID.
        @return: One book from the database.
        """
        return BookSchema().dump(book_service.get_one(bid)), 200

    def put(self, bid):
        """
        PUT (full update)
        @param bid: Book ID.
        @return: 200 Ok. Full update one book from the database.
        """
        req_json = request.json
        book_service.update(req_json)
        return "method:put", 200

    # def patch(self, bid):
    #     """
    #     PATCH (partial update)
    #     @param bid: Book ID.
    #     @return: 200 Ok. Partial update one book from the database.
    #     """
    #     req_json = request.json
    #     req_json["book_id"] = bid
    #     book_service.update(req_json)
    #     return "method:patch", 200

    def delete(self, bid):
        """
        DELETE.
.
        @param bid: Book ID.
        @return: 204 No content. Delete book from the database.
        """
        book_service.delete(bid)
        return "method:delete", 204

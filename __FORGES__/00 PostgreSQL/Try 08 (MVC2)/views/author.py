from flask_restx import Resource, Namespace

from dao.model.author import AuthorSchema
from implemented import author_service

author_ns = Namespace('authors')


@author_ns.route('/')
class AuthorsView(Resource):
    def get(self):
        """
        GET ALL.
        @return: All authors from the database.
        """
        return AuthorSchema(many=True).dump(author_service.get_all()), 200


@author_ns.route('/<int:aid>/')
class AuthorView(Resource):
    def get(self, aid):
        """
        GET ONE.
        @param aid: Author ID.
        @return: One author from the database.
        """
        return AuthorSchema().dump(author_service.get_one(aid)), 200

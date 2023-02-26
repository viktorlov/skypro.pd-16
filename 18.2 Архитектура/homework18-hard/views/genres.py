from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self) -> tuple[list, int]:
        genres = genre_service.get_all()
        result: list = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def get(self, gid: int) -> tuple[list, int]:
        genre = genre_service.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200

from flask_restx import Resource, Namespace

from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self) -> tuple[list, int]:
        """
        Получение всех кортежей из таблицы genre.
        """
        genres = db.session.query(Genre).all()
        result: list = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route('/<int:gid>/')
class GenreView(Resource):
    def get(self, gid) -> tuple[list, int]:
        """
        Получение одного кортежа из таблицы genre по id.
        """
        genre = db.session.query(Genre).get(gid)
        result: list = GenreSchema().dump(genre)
        return result, 200

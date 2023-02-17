from flask_restx import Resource, Namespace

from models import Director, DirectorSchema
from setup_db import db

director_ns: Namespace = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self) -> tuple[list, int]:
        """
        Получение всех кортежей из таблицы director.
        """
        directors = db.session.query(Director).all()
        result: list = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did: int) -> tuple[list, int]:
        """
        Получение одного кортежа из таблицы director по id.
        """
        director = db.session.query(Director).get(did)
        result: list = DirectorSchema().dump(director)
        return result, 200

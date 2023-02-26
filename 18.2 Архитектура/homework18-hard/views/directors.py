from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self) -> tuple[list, int]:
        directors = director_service.get_all()
        result: list = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did: int) -> tuple[list, int]:
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200

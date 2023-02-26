# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self) -> tuple[list, int]:
        directors = director_service.get_all()
        result: list = DirectorSchema(many=True).dump(directors)
        return result, 200

    @admin_required
    def post(self) -> tuple[str, int, dict[str, str]]:
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    @auth_required
    def get(self, did: int) -> tuple[list, int]:
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200

    @admin_required
    def put(self, did: int) -> tuple[str, int]:
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did: int) -> tuple[str, int]:
        director_service.delete(did)
        return "", 204

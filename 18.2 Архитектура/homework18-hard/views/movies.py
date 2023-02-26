from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self) -> tuple[list, int]:
        director: str | None = request.args.get("director_id")
        genre: str | None = request.args.get("genre_id")
        year: str | None = request.args.get("year")
        filters: dict[str, str | None] = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        movies = movie_service.get_all(filters)
        result: list = MovieSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204

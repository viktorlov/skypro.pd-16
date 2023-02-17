from flask import request
from flask_restx import Resource, Namespace

from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self) -> tuple[list, int]:
        """
        Получение всех записей из таблицы movie.
        Опциональные параметры:
            - режиссёр (по id);
            - жанр (по id);
            - год выпуска (по year).
        Возможно любое сочетание опциональных параметров.
        """
        director: str | None = request.args.get("director_id")
        genre: str | None = request.args.get("genre_id")
        year: str | None = request.args.get("year")
        interim = db.session.query(Movie)
        if director is not None:
            interim = interim.filter(Movie.director_id == director)
        if genre is not None:
            interim = interim.filter(Movie.genre_id == genre)
        if year is not None:
            interim = interim.filter(Movie.year == year)
        all_movies = interim.all()
        result: list = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self) -> tuple[str, int] | tuple[dict[str, str], int]:
        """
        Запись в таблицу movie нового кортежа.
        """
        new_movie_data = request.json
        new_movie: Movie = Movie(**new_movie_data)
        try:
            db.session.add(new_movie)
            db.session.commit()
            return "", 201
        except Exception as e:
            return {'message': str(e)}, 500


@movie_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid: int) -> tuple[list, int]:
        """
        Получение одного кортежа из таблицы movie по id.
        """
        movie = db.session.query(Movie).get(mid)
        result: list = MovieSchema().dump(movie)
        return result, 200

    def put(self, mid: int) -> tuple[str, int]:
        """
        Обновление кортежа в таблице movie по id.
        """
        updated_movie = db.session.query(Movie).filter(Movie.id == mid).update(request.json)
        if not updated_movie:
            return f"Фильм с индексом {mid} не найден.", 400
        db.session.commit()
        return "", 204

    def delete(self, mid) -> tuple[str, int] | tuple[dict[str, str], int]:
        """
        Удаление кортежа в таблице movie по id.
        """
        try:
            movie = db.session.query(Movie).get(mid)
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500

from flask_restx import Resource, Namespace
from flask import request
from app.database import db
from models import MovieSchema, Movie

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route("/")
class MoviesView(Resource):
    """
    Методы <<GET>> и <<POST>> для "/movies/"
    """

    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        if director and genre is not None:
            movies = Movie.query.filter(Movie.director_id == director).filter(Movie.genre_id == genre)
        elif genre is not None:
            movies = Movie.query.filter(Movie.genre_id == genre)
        elif director is not None:
            movies = Movie.query.filter(Movie.director_id == director)
        else:
            movies = db.session.query(Movie).all()
        return movies_schema.dump(movies), 200

    def post(self):
        new_movie_data = request.json
        new_movie = Movie(**new_movie_data)
        try:
            with db.session.begin():
                db.session.add(new_movie)
            return f"Фильм '{new_movie.title}' добавлен в базу с индексом {new_movie.id}.", 201
        except Exception as e:
            return {'message': str(e)}, 500


@movies_ns.route("/<int:mid>/")
class MovieView(Resource):
    """
    Методы <<GET>>, <<PUT>>, <<DELETE>> для "movies/<int:mid>/"
    """

    def get(self, mid: int):
        movie = Movie.query.get(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        updated_movie = db.session.query(Movie).filter(Movie.id == mid).update(request.json)
        if not updated_movie:
            return f"Фильм с индексом {mid} не найден.", 400
        db.session.commit()
        return "", 204

    def delete(self, mid: int):
        movie = Movie.query.get(mid)
        try:
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500
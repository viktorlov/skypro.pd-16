from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

from bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from config import ProjectConfig

app = Flask(__name__)
app.register_blueprint(errorhandlers)
app.config.from_object(ProjectConfig)
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    director_id = fields.Int()
    genre_id = fields.Int()
    director = fields.Pluck("DirectorSchema", "name")
    genre = fields.Pluck("GenreSchema", "name")


class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_schema = DirectorSchema()
genres_schema = DirectorSchema(many=True)

api = Api(app)

movies_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


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


@director_ns.route("/")
class DirectorView(Resource):
    """
    Методы <<GET>> и <<POST>> для "/directors/"
    POST directors:
        {
            id: Int,
            name: Str
        }
    """

    def get(self):
        movie = Director.query.all()
        return directors_schema.dump(movie), 200

    def post(self):
        new_director_data = request.json
        new_director = Director(**new_director_data)
        try:
            with db.session.begin():
                db.session.add(new_director)
            return f"Директор {new_director.name} добавлен в базу с индексом {new_director.id}.", 201
        except Exception as e:
            return {'message': str(e)}, 500


@director_ns.route("/<int:did>/")
class DirectorView(Resource):
    """
    Методы <<GET>>, <<PUT>> и <<DELETE>> для "directors/<int:did>/"
    """

    def get(self, did: int):
        director = Director.query.get(did)
        return director_schema.dump(director), 200

    def put(self, did: int):
        updated_director = db.session.query(Director).filter(Director.id == did).update(request.json)
        if not updated_director:
            return f"Директор с индексом {did} не найден.", 400
        db.session.commit()
        return "", 204

    def delete(self, did: int):
        director = Director.query.get(did)
        try:
            db.session.delete(director)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500


@genre_ns.route("/")
class GenreView(Resource):
    """
    Методы <<GET>> и <<POST>> для "/genres/"
    """

    def get(self):
        genres_all = Genre.query.all()
        return genres_schema.dump(genres_all), 200

    def post(self):
        new_genre_data = request.json
        new_genre = Genre(**new_genre_data)
        try:
            with db.session.begin():
                db.session.add(new_genre)
            return f"Жарн {new_genre.name} добавлен в базу с индексом {new_genre.id}.", 201
        except Exception as e:
            return {'message': str(e)}, 500


@genre_ns.route("/<int:gid>/")
class GenreView(Resource):
    """
    Методы <<GET>>, <<PUT>> и <<DELETE>> для "genre/<int:gid>/"
    """

    def get(self, gid: int):
        movie = Genre.query.get(gid)
        return genre_schema.dump(movie), 200

    def put(self, gid: int):
        updated_genre = db.session.query(Genre).filter(Genre.id == gid).update(request.json)
        if not updated_genre:
            return f"Жанр с индексом {gid} не найден.", 400
        db.session.commit()
        return "", 204

    def delete(self, gid: int):
        genre = Genre.query.get(gid)
        try:
            db.session.delete(genre)
            db.session.commit()
            return "", 204
        except Exception as e:
            return {'message': str(e)}, 500


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

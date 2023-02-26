from flask import Flask
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
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        """
        @return: Получение всех - вернет “Получение всех”, код 200
        """
        return 'Получение всех', 200

    def post(self):
        """
        @return: Добавление нового - вернет “Добавление нового ”, код 201
        """
        return 'Добавление нового', 201


@movies_ns.route("/<int:mid>/")
class MovieView(Resource):
    def get(self, mid: int):
        """
        @param mid: Movie id
        @return: Получение одного по ключу - вернет “Получение по ключу”, код 200
        """
        return f'Получение по ключу {mid}', 200

    def put(self, mid: int):
        """
        @param mid: Movie id
        @return: Частичное обновление - вернет “Частичное обновление по ключу”, код 200
        """
        return f'Частичное обновление по ключу {mid}', 201

    def delete(self, mid: int):
        """
        @param mid: Movie id
        @return: Удаление - вернет “Удаление по ключу”, код 204
        """
        return f'Удаление по ключу {mid}', 200


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

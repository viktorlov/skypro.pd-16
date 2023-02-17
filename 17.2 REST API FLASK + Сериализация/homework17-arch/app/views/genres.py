from flask_restx import Resource, Namespace
from flask import request
from app.database import db
from models import GenreSchema, Genre

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route("/")
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


@genres_ns.route("/<int:gid>/")
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

from flask_restx import Resource, Namespace
from flask import request
from app.database import db
from models import DirectorSchema, Director

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route("/")
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


@directors_ns.route("/<int:did>/")
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

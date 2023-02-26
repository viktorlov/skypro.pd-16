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


class Toy(db.Model):
    __tablename__ = 'toy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class ToySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


toy_schema = ToySchema()
toys_schema = ToySchema(many=True)

api = Api(app)

toys_ns = api.namespace('toys')


@toys_ns.route("/")
class ToysView(Resource):
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


@toys_ns.route("/<int:tid>/")
class ToyView(Resource):
    def get(self, tid: int):
        """
        @param tid: Toy id
        @return: Получение одного по ключу - вернет “Получение по ключу”, код 200
        """
        return f'Получение по ключу {tid}', 200


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

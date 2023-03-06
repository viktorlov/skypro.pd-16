from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

User_ns = Namespace('Users')


@User_ns.route('/')
class UsersView(Resource):
    def get(self):
        Users = user_service.get_all()
        return UserSchema(many=True).dump(Users), 200

    def post(self):
        req_json = request.json
        ent = user_service.create(req_json)
        return "", 201, {"location": f"/users/{ent.id}"}


@User_ns.route('/<int:bid>')
class UserView(Resource):
    def get(self, bid):
        User = user_service.get_one(bid)
        return UserSchema().dump(User), 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        user_service.update(req_json)
        return "", 204

    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        user_service.partially_update(req_json)
        return "", 204

    def delete(self, bid):
        user_service.delete(bid)
        return "", 204

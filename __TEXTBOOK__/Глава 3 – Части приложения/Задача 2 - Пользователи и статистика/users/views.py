from flask import Blueprint, jsonify, request

users = Blueprint('users', __name__)


@users.get('/')
def get():
    from users.utils import read_json
    return jsonify(read_json())

@users.post('/')
def post():
    from users.utils import write_json
    users_to_add = request.json
    return jsonify(write_json(users_to_add))
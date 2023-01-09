from flask import Blueprint, request, jsonify

profiles = Blueprint('profiles', __name__)

users_all = [{"pk": 1, "name": "alex", "phone": "+123456789"},
             {"pk": 2, "name": "mary", "phone": "+987654321"}, ]


@profiles.get('/')
def get():
    return f'{request.url}'


@profiles.get('/<int:id>')
def get_profile(id):
    output = {}
    for row in users_all:
        if row['pk'] == id:
            output.update(row)
            break
    return jsonify(output)

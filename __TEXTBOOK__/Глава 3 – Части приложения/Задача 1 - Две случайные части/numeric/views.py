from flask import Blueprint

numeric = Blueprint('numeric', __name__)


@numeric.get('/random/')
def random_number():
    from random import randint
    from flask import jsonify
    return jsonify({'number': randint(1, 10)})

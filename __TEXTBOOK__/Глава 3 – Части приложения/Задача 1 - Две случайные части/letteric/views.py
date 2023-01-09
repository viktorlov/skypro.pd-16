from flask import Blueprint

letteric = Blueprint('letteric', __name__)


@letteric.get('/random/')
def random_letter():
    from string import ascii_lowercase
    from random import choice
    from flask import jsonify
    return jsonify({'letter': choice(list(ascii_lowercase))})

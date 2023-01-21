from flask import Flask, jsonify

import utils
from bp_errorhandlers.bp_errorhandlers_views import errorhandlers

app = Flask(__name__)

app.config.from_pyfile('config/config.py')

app.register_blueprint(errorhandlers)


@app.get('/')
def page_index():
    return "Index", 200


@app.get('/movie/<title>/')
def page_movie_by_title(title):
    data = utils.get_movie_by_title(title)
    return jsonify(data), 200


@app.get('/movie/<int:start>/to/<int:end>/')
def page_movies_by_years(start, end):
    data = utils.get_movies_by_years(start, end)
    return jsonify(data), 200


@app.get('/rating/<category>/')
def page_get_by_category(category):
    data = utils.get_movies_by_category(category)
    return jsonify(data), 200


@app.get('/genre/<genre>/')
def page_get_by_genre(genre):
    data = utils.get_movies_by_genre(genre)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))

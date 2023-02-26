from flask import Flask, jsonify, request

from bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from config import ProjectConfig

app = Flask(__name__)
app.register_blueprint(errorhandlers)
app.config.from_object(ProjectConfig)

movies = [{
    "title": "Йеллоустоун",
    "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
    "year": 2018,
    "rating": 8.6,
    "pk": 1
}, {
    "title": "Омерзительная восьмерка",
    "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
    "year": 2015,
    "rating": 7.8,
    "genre_id": 4,
    "pk": 2
}, {
    "title": "Вооружен и очень опасен",
    "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
    "year": 1978,
    "rating": 6,
    "pk": 3
}
]


@app.route('/movies/', methods=["GET", "POST"])
def page_index():
    if request.method == 'GET':
        return jsonify(movies)
    if request.method == 'POST':
        added_movie = request.json
        if added_movie['pk'] not in [row['pk'] for row in movies]:
            movies.append(added_movie)
            return jsonify(added_movie), 201
        else:
            return jsonify({'error': f'Movie ID {added_movie["pk"]} is already exists'}), 500


@app.route('/movies/<int:mid>/', methods=["GET"])
def page_get(mid):
    if request.method == 'GET':
        for row in movies:
            if row['pk'] == mid:
                return jsonify(row), 200
        else:
            return jsonify({'error': f'Invalid ID {mid}'}), 500


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

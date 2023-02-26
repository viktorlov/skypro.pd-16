from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

from bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from config import ProjectConfig

app = Flask(__name__)
app.register_blueprint(errorhandlers)
app.config.from_object(ProjectConfig)
db = SQLAlchemy(app)

movies_data = [{
    "title": "Йеллоустоун",
    "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
    "year": 2018,
    "rating": 8.6,
    "id": 1
}, {
    "title": "Омерзительная восьмерка",
    "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
    "year": 2015,
    "rating": 7.8,
    "id": 2
}, {
    "title": "Вооружен и очень опасен",
    "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
    "year": 1978,
    "rating": 6,
    "id": 3
}
]


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@app.route("/")
def init_page():
    db.drop_all()
    db.create_all()
    movies = [Movie(**movie) for movie in movies_data]
    db.session.add_all(movies)
    db.session.commit()
    return "База данных создана"


@app.route("/movies/")
def get_all_movies():
    movies_data = Movie.query.all()
    movies = movies_schema.dump(movies_data)
    return jsonify(movies), 200


@app.route("/movies/<int:mid>/")
def get_one_movie(mid):
    movie_data = Movie.query.get(mid)
    movie = movie_schema.dump(movie_data)
    return jsonify(movie), 200


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

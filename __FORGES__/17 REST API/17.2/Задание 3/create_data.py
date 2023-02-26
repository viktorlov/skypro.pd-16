from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toys.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Toy(db.Model):
    __tablename__ = 'toy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


db.drop_all()
db.create_all()

# -------------------------------------------------------
data = {
    "toys": [
        {"name": "Комедия", "pk": 1},
        {"name": "Семейный", "pk": 2},
        {"name": "Фэнтези", "pk": 3},
        {"name": "Драма", "pk": 4},
        {"name": "Приключения", "pk": 5},
        {"name": "Триллер", "pk": 6},
        {"name": "Фантастика", "pk": 7},
        {"name": "Аниме", "pk": 8},
        {"name": "Документальное", "pk": 9},
        {"name": "Короткометражка", "pk": 10},
        {"name": "Ужасы", "pk": 11},
        {"name": "Боевик", "pk": 12},
        {"name": "Мелодрама", "pk": 13},
        {"name": "Детектив", "pk": 14},
        {"name": "Авторское кино", "pk": 15},
        {"name": "Мультфильм", "pk": 16},
        {"name": "Вестерн", "pk": 17},
        {"name": "Мюзикл", "pk": 18}],
}
# -------------------------------------------------------

for toy in data["toys"]:
    each = Toy(id=toy["pk"],
               name=toy["name"])
    with db.session.begin():
        db.session.add(each)

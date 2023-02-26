def db_create_all():

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./fruits.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db = SQLAlchemy(app)

    class Fruit(db.Model):
        __tablename__ = 'fruits'
        pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
        icon = db.Column(db.String(6))
        name = db.Column(db.String(50))
        category = db.Column(db.String(50))
        kcal = db.Column(db.Integer())

    db.drop_all()
    db.create_all()

    mock_fruits = [Fruit(icon="🍏", name="Apple", category="fruit", kcal=38),
                   Fruit(icon="🍎", name="RedApple", category="fruit", kcal=40),
                   Fruit(icon="🍌", name="Banana", category="fruit", kcal=96),
                   Fruit(icon="🥑", name="Avocado", category="fruit", kcal=160),
                   Fruit(icon="🍅", name="Tomato", category="veggie", kcal=23),
                   Fruit(icon="🥦", name="Broccoli", category="veggie", kcal=34),
                   Fruit(icon="🥕", name="Carrot", category="veggie", kcal=41),
                   Fruit(icon="🍪", name="Cookie", category="sweets", kcal=417),
                   Fruit(icon="🍩", name="Donut", category="sweets", kcal=280),
                   Fruit(icon="🍰", name="Cake", category="sweets", kcal=271)]

    db.session.add_all(mock_fruits)
    db.session.commit()


if __name__ == '__main__':
    db_create_all()

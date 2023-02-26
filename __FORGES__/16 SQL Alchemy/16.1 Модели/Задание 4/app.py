import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Flight(db.Model):
    __tablename__ = 'flights'
    number = db.Column(db.String(6), primary_key=True)
    airport_from = db.Column(db.String(3))
    airport_to = db.Column(db.String(3))
    aircraft = db.Column(db.Boolean())


db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from flights").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)

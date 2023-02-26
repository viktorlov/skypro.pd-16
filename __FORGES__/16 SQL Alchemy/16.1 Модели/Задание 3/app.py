import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Room(db.Model):
    __tablename__ = 'rooms'
    pk = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String())
    room_type = db.Column(db.String())
    is_booked = db.Column(db.Boolean())



db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from rooms").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)

import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Message(db.Model):
    __tablename__ = 'messages'
    pk = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String())
    to = db.Column(db.String())
    content = db.Column(db.String())
    status = db.Column(db.String())


db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from messages").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)

import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class ProgrammingLanguage(db.Model):
    __tablename__ = 'languages'
    pk = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(20))
    invented_at = db.Column(db.Integer())
    is_nice = db.Column(db.Boolean())
    is_modern = db.Column(db.Boolean())
    is_popular = db.Column(db.Boolean())


db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from languages").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)

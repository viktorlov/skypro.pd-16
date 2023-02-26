from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

from bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from config import ProjectConfig

app = Flask(__name__)
app.register_blueprint(errorhandlers)
app.config.from_object(ProjectConfig)
db = SQLAlchemy(app)

users_data = [
    {'id': 1, 'first_name': 'Hudson', 'last_name': 'Pauloh', 'age': 31, 'email': 'elliot16@mymail.com',
     'role': 'customer', 'phone': '6197021684'},
    {'id': 2, 'first_name': 'George', 'last_name': 'Matter', 'age': 41, 'email': 'lawton46@mymail.com',
     'role': 'executor', 'phone': '8314786677'},
    {'id': 3, 'first_name': 'Grant', 'last_name': 'Traviser', 'age': 23, 'email': 'tobias45@mymail.com',
     'role': 'customer', 'phone': '9528815998'}
]


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    role = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))


class UserSchema(Schema):
    id = fields.Int()
    age = fields.Int()
    role = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Str()
    phone = fields.Str()


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/")
def init_page():
    db.drop_all()
    db.create_all()
    users = [User(**user) for user in users_data]
    db.session.add_all(users)
    db.session.commit()
    return "База данных создана"


@app.route("/users/")
def get_users():
    users_data = User.query.all()
    users = users_schema.dump(users_data)
    return jsonify(users)


@app.route("/users/<int:mid>/")
def get_one_user(mid):
    user_data = User.query.get(mid)
    user = user_schema.dump(user_data)
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=ProjectConfig.DEBUG,
            host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

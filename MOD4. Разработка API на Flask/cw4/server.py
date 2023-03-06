# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask import Flask, jsonify
from flask_cors import CORS

from errorhandlers.views import errorhandlers
from exceptions import BaseServiceError
from setup.api import api
from setup.db import db
from views import auth_ns, genres_ns, user_ns, directors_ns, movies_ns, favorites_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.get('/')
    def index():
        return "<h1>Курс 4. Курсовая работа</h1><br>" \
               "<h3>Привет, с вами Рид Хастингс!</h3>И сегодня мы будем делать свой «Кинопоиск» с кучей разных фильмов!<br>" \
               "Эта курсовая потребует знания Flask, SQLAlchemy, Marshmallow, REST, CRUD, JWT и, конечно же, знаний и умений правильного создания структуры проекта.<br>" \
               "В данной работе вы можете использовать либо свой написанный бек, либо использовать исходники, которые предоставлены <a href=https://github.com/skypro-008/coursework_3_source target=_blank>здесь</a>.<br><br>" \
               "1) <a href=/movies/ target=_blank>GET all movies</a><br>" \
               "2) <a href=/movies/?page=2 target=_blank>GET all movies page 2</a><br>" \
               "3) <a href=/movies/?status=new target=_blank>GET all new movies</a><br>" \
               "4) <a href=/movies/?status=new&page=2 target=_blank>GET all new movies page 2</a><br>" \
               "5) <a href=/movies/2/ target=_blank>GET movie ID 2</a><br>" \
               "6) <a href=/genres/ target=_blank>GET all genres</a><br>" \
               "7) <a href=/genres/4/ target=_blank>GET genre 4</a><br>" \
               "8) <a href=/directors/ target=_blank>GET all directors</a><br>" \
               "9) <a href=/directors/2/ target=_blank>GET director ID 2</a><br>"

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(favorites_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)
    app.register_blueprint(errorhandlers)

    return app

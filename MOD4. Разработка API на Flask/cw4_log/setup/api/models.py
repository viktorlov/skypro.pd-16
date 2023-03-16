# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
from flask_restx import fields, Model

from setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссёр', {
    'id': fields.Integer(required=True, example=2),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино')
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=2),
    'title': fields.String(required=True, example='Омерзительная восьмерка'),
    'description': fields.String(required=True,
                                 example='США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.'),
    'trailer': fields.String(required=True, example='https://www.youtube.com/watch?v=lmB9VWm0okU'),
    'year': fields.Integer(required=True, example=2015),
    'rating': fields.Float(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=4),
    'email': fields.String(required=True, max_length=100, example='director@hogwarts.hsww'),
    'password': fields.String(required=True, example='xrgZeizAzjMltX1HdwLFjkKJmbFV5teXx2Hzb0qVa4o='),
    'name': fields.String(required=True, example='Albus'),
    'surname': fields.String(required=True, example='Dumbledore'),
    'favorite_genre': fields.Nested(genre)
})

favorite_movie: Model = api.model('Избранные фильмы', {
    'id': fields.Integer(required=True, example=2),
    'user': fields.Nested(user),
    'movie': fields.Nested(movie)
})

from flask_restx import Api

from .directors_ns import directors_api
from .genres_ns import genres_api
from .movie_ns import movies_api

api = Api(title='Lesson_17',
          description='Урок 17. REST API на Flask. Домашнее задание.')

api.add_namespace(movies_api)
api.add_namespace(directors_api)
api.add_namespace(genres_api)

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.book import book_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    configure_app(app)
    return app


def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(book_ns)


app = create_app(Config())
# app.debug = True

if __name__ == '__main__':
    app.run(host=Config().HOST,
            port=Config().PORT)

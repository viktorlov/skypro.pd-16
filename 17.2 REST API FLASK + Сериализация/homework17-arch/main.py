from flask import Flask
from flask_restx import Api

from app.config import ProjectConfig
from app.database import db
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns
from errorhandlers.views import errorhandlers


def create_app(config: ProjectConfig) -> Flask:
    application = Flask(__name__)
    application.register_blueprint(errorhandlers)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask) -> None:
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


if __name__ == '__main__':
    app_config = ProjectConfig()
    app = create_app(app_config)
    configure_app(app)
    app.run(host=ProjectConfig.HOST,
            port=ProjectConfig.PORT)

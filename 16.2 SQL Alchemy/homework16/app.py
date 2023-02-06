from os import path, mkdir

import sqlalchemy.exc
from flask import Flask

from bp_errorhandlers.bp_errorhandlers_views import errorhandlers
from config import Config, LOGS_FOLDER, HOST, PORT
from create_data.database_loader import create_data_for_table
from logger_config import get_logger
from models import db, User, Offer, Order
from offers import offers_blueprint
from orders import orders_blueprint
from users import users_blueprint

if not path.exists(LOGS_FOLDER):
    mkdir(LOGS_FOLDER)
logger = get_logger(__name__, 'logs/app.log')


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(orders_blueprint)
    app.register_blueprint(offers_blueprint)
    app.register_blueprint(errorhandlers)
    return app


def setup_database(app: Flask) -> None:
    with app.app_context():
        db.drop_all()
        db.create_all()
        try:
            create_data_for_table('loader/user.json', User)
            create_data_for_table('loader/offer.json', Offer)
            create_data_for_table('loader/order.json', Order)
        except sqlalchemy.exc.PendingRollbackError as e:
            logger.debug(str(e))
            pass


if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run(host=HOST, port=PORT)

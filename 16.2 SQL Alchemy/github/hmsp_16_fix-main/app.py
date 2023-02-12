from utils.funtions import starting_flask
from blueprints.user.user import user
from blueprints.order.order import order
from blueprints.offer.offer import offer

from utils.funtions import database_user, database_order, database_offer
from utils.models import User, Order, Offer

from setup_db import db

# В переменной app находится функция для запуска приложения.
app = starting_flask()

app.register_blueprint(user)
app.register_blueprint(order)
app.register_blueprint(offer)

with app.app_context():

    database_user(db, User)
    database_offer(db, Offer)
    database_order(db, Order)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

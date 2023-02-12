from flask_sqlalchemy import SQLAlchemy
from utils.funtions import starting_flask,\
                     database_user, \
                     database_offer, \
                     database_order

from setup_db import db


# db = starting_flask()


class User(db.Model):
    '''
    В модели User находятся необходимые переменные для таблицы user,
    которые имеют созвучные названия
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key='True')
    first_name = db.Column(db.Text(50), nullable=False)
    last_name = db.Column(db.Text(50))
    age = db.Column(db.Integer, db.CheckConstraint('age >= 18'))
    email = db.Column(db.Text(100), unique=True)
    role = db.Column(db.Text(100))
    phone = db.Column(db.Text(50))


    def to_dict_user(self):
        '''
        Метод to_dict_user преобразует данные из таблицы в формат словаря
        '''
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone
        }


    def __repr__(self):
        return f'User: ' \
               f'{self.id}, ' \
               f'{self.first_name}'


class Offer(db.Model):
    '''
    В модели Offer находятся необходимые переменные для таблицы offer,
    которые имеют созвучные названия.
    В переменные order_id и executor_id вносим значения для связи с
    таблицей order и user соответственно.
    '''
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key='True')
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict_offer(self):
        '''
        Метод to_dict_offer преобразует данные из таблицы в формат словаря
        '''
        return {
            'id': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id
        }

    def __repr__(self):
        return f'Offer: ' \
               f'{self.id}, ' \
               f'{self.order_id}, ' \
               f'{self.executor_id}'


class Order(db.Model):
    '''
    В модели Offer находятся необходимые переменные для таблицы offer,
    которые имеют созвучные названия.
    В переменные customer_id и executor_id вносим значения для связи с
    таблицей user.
    '''
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key='True')
    name = db.Column(db.Text(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)
    address = db.Column(db.Text)
    price = db.Column(db.Numeric, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def to_dict_order(self):
        '''
        Метод to_dict_offer преобразует данные из таблицы в формат словаря
        '''
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price,
            'customer_id': self.customer_id,
            'executor_id': self.executor_id
        }


    def __repr__(self):
        return f'Order: ' \
               f'{self.id}, ' \
               f'{self.name}, ' \
               f'{self.customer_id}, ' \
               f'{self.executor_id}'



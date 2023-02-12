import json
from flask import request
from flask import Blueprint

from setup_db import db
from utils.models import Order


order = Blueprint(
    'order',
    __name__,
    template_folder='templates/order',
    static_folder='static'
)
'''
В переменную order закладываем blueprint, который будем использовать
в основном файле программы. 
'''


@order.route('/orders', methods=['GET', 'POST'])
def orders():

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод всех пользователей.
        '''
        result = []
        for order in Order.query.all():
            result.append(order.to_dict_order())
        return f'<h1>List of all orders!</h1>' \
               f'{json.dumps(result)}', 200

    if request.method == 'POST':
        '''
        Проверка запроса и последующее добавление нового пользователя.
        '''
        order_data = json.loads(request.data)
        new_order = Order(
            id = order_data['id'],
            name = order_data['name'],
            description = order_data['description'],
            start_date = order_data['start_date'],
            end_date = order_data['end_date'],
            address = order_data['address'],
            price = order_data['price'],
            customer_id =  order_data['customer_id'],
            executor_id = order_data['executor_id']
        )

        db.session.add(new_order)
        db.session.commit()

        return f'<h1>Order created!</h1>', 201


@order.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def order_id(uid: int):

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод одного пользователя по id.
        '''
        return f'<h1>Order with {uid} found!</h1>' \
               f'{json.dumps(Order.query.get(uid).to_dict_order())}', 200

    if request.method == 'PUT':
        '''
        Проверка запроса и последующее обновление данных уже
        существующего пользователя.
        '''
        order_data = json.loads(request.data)
        order = Order.query.get(uid)
        order.name = order_data['name'],
        order.description = order_data['description'],
        order.start_date = order_data['start_date'],
        order.end_date = order_data['end_date'],
        order.address = order_data['address'],
        order.price = order_data['price'],
        order.customer_id = order_data['customer_id'],
        order.executor_id = order_data['executor_id']

        db.session.add(order)
        db.session.commit()

        return f'<h1>Order {uid} updated!</h1>', 204

    if request.method == 'DELETE':
        '''
        Проверка запроса и последующее удаление одного пользователя по id.
        '''
        order = Order.query.get(uid)

        db.session.delete(order)
        db.session.commit()

        return f'<h1>Order {uid} deleted!</h1>', 204

import json
from flask import request
from flask import Blueprint

from setup_db import db

from utils.models import Offer


offer = Blueprint(
    'offer',
    __name__,
    template_folder='templates/offer',
    static_folder='static'
)
'''
В переменную offer закладываем blueprint, который будем использовать
в основном файле программы. 
'''


@offer.route('/offers', methods=['GET', 'POST'])
def offers():

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод всех пользователей.
        '''
        result = []
        for offer in Offer.query.all():
            result.append(offer.to_dict_offer())
        return f'<h1>List of all offers!</h1>' \
               f'{json.dumps(result)}', 200

    if request.method == 'POST':
        '''
        Проверка запроса и последующее добавление нового пользователя.
        '''
        offer_data = json.loads(request.data)
        new_offer = Offer(
            id = offer_data['id'],
            order_id =  offer_data['order_id'],
            executor_id = offer_data['executor_id']
        )

        db.session.add(new_offer)
        db.session.commit()

        return f'<h1>Offer created!</h1>', 201


@offer.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def offer_id(uid: int):

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод одного пользователя по id.
        '''
        return f'<h1>Offer with {uid} found!</h1>' \
               f'{json.dumps(Offer.query.get(uid).to_dict_offer())}', 200

    if request.method == 'PUT':
        '''
        Проверка запроса и последующее обновление данных уже
        существующего пользователя.
        '''
        offer_data = json.loads(request.data)
        offer = Offer.query.get(uid)
        offer.order_id = offer_data['order_id'],
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        return f'<h1>Offer {uid} updated!</h1>', 204

    if request.method == 'DELETE':
        '''
        Проверка запроса и последующее удаление одного пользователя по id.
        '''
        offer = Offer.query.get(uid)

        db.session.delete(offer)
        db.session.commit()

        return f'<h1>Offer {uid} deleted!</h1>', 204

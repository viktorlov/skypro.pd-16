import json
from flask import request
from flask import Blueprint
from setup_db import db

from utils.models import User


user = Blueprint(
    'user',
    __name__,
    template_folder='templates/user',
    static_folder='static'
)
'''
В переменную user закладываем blueprint, который будем использовать
в основном файле программы. 
'''


@user.route('/users', methods=['GET', 'POST'])
def users():

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод всех пользователей.
        '''
        result = []
        for user in User.query.all():
            result.append(user.to_dict_user())
        return f'<h1>List of all users!</h1>' \
               f'{json.dumps(result)}', 200

    if request.method == 'POST':
        '''
        Проверка запроса и последующее добавление нового пользователя.
        '''
        user_data = json.loads(request.data)
        new_user = User(
            id = user_data['id'],
            first_name = user_data['first_name'],
            last_name = user_data['last_name'],
            age = user_data['age'],
            email = user_data['email'],
            role = user_data['role'],
            phone = user_data['phone']
        )

        db.session.add(new_user)
        db.session.commit()

        return f'<h1>User created!</h1>', 201


@user.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def user_id(uid: int):

    if request.method == 'GET':
        '''
        Проверка запроса и последующий вывод одного пользователя по id.
        '''
        return f'<h1>User with {uid} found!</h1>' \
               f'{json.dumps(User.query.get(uid).to_dict_user())}', 200

    if request.method == 'PUT':
        '''
        Проверка запроса и последующее обновление данных уже
        существующего пользователя.
        '''
        user_data = json.loads(request.data)
        user = User.query.get(uid)
        user.first_name = user_data['first_name'],
        user.last_name = user_data['last_name'],
        user.age = user_data['age'],
        user.email = user_data['email'],
        user.role = user_data['role'],
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        return f'<h1>User {uid} updated!</h1>', 204

    if request.method == 'DELETE':
        '''
        Проверка запроса и последующее удаление одного пользователя по id.
        '''
        user = User.query.get(uid)

        db.session.delete(user)
        db.session.commit()

        return f'<h1>User {uid} deleted!</h1>', 204

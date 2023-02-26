# Написать функцию `generate_jwt` которая 
# генерирует access_token и refresh_token.
# В качестве аргумента функция должна принимать словарь вида user_obj.
# Для формирования токена используйте алгоритм 'HS256' и ключ 's3cR$eT'.
# В access и в refresh токене должна содержаться информация об:
# 1. имени пользователя ('username')
# 2. роли ('role')
# 3. времени действия токена ('exp')
# Время действия access токена должно составлять 30 с момента получения
# Время действия refresh токена - 130 дней c момента получения

import calendar
import datetime

import jwt

SECRET = "s3cR$eT"
ALGO = "HS256"

user_obj = {
    "username": 'test_user',
    "role": 'admin'
}


def generate_jwt(user_obj):
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)

    user_obj["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(user_obj, SECRET, algorithm=ALGO)
    user_obj["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(user_obj, SECRET, algorithm=ALGO)

    return dict(access_token=access_token, refresh_token=refresh_token)


if __name__ == '__main__':
    print(generate_jwt(user_obj))

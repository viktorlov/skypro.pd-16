'''
Функции для чтения и записи json-файлы
'''

import json


def read_json():
    with open('users.json', "r") as file:
        users_list = json.load(file)

    return users_list


def write_json(arg):
    users_list = read_json()
    len_ = 0

    if type(arg) is dict:
        users_list.append(arg)
        len_ = 1

    if type(arg) is list:
        for each in arg:
            users_list.append(each)
        len_ = len(arg)

    with open('users.json', 'w') as file:
        json.dump(users_list, file)

    return {'status': 'ok', 'added': len_}

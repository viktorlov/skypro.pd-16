"""
Функции для получения статистики json-файла
"""


def count_users():
    import json
    with open('users.json', "r") as file:
        users_list = json.load(file)
    return {'count': len(users_list)}


if __name__ == '__main__':
    print(count_users())

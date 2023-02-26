# У вас есть словарь, который содержит 
# данные о пользователе. На его основе 
# сгенерируйте токен. 
#
# В качестве секрета используйте слово 's3cR$eT',
# В качестве алгоритма формирования токена используйте 'HS256'.
# Сгенерированный токен запишите в переменную access_token.

import jwt

data = {
    "username": "Skypro",
    "role": "admin"
}

SECRET = "s3cR$eT"
ALGO = "HS256"


def generate_token(token_data):
    # min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    # token_data["EXP"] = calendar.timegm(min30.timetuple())
    return jwt.encode(token_data, SECRET, algorithm=ALGO)


access_token = generate_token(data)

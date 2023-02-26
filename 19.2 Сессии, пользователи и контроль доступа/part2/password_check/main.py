# Просто: Напишите функцию, которая получает пароль 
# в открытом виде первым аргументом и хеш вторым аргументом.
# После чего берет хеш от пароля в открытом виде и сравнивает хеши.
# При хэшировании необходимо использовать алгоритм md5
#
# Для удобства самопроверки мы предоставляем вам пароль в открытом виде:
# H4RDP4S$w0rd
# и хеш в формате md5:
# 80309097b712c6828d0f3f6dfd713e80
#
# ##############################################
# Сложно: Напишите функцию, которая получает пароль 
# в открытом виде, хеш, соль и алгоритм хеширования, 
# берет хеш от пароля в открытом виде и сравнивает хеши
#
# Для самопроверки:
#
# Пароль:
# H4RDP4S$w0rd
#
# Хэш sha256:
# b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb'
#
# Соль:
# Skypro
#
# Число итераций: 1000

import hashlib
import hmac


def easy(pwd_hash, other_password: str):
    other_password = hashlib.md5(other_password.encode("utf-8")).hexdigest()
    return pwd_hash == other_password


def hard(password_hash, other_password, salt, algo):
    other_password = hashlib.pbkdf2_hmac(algo, other_password.encode("utf-8"), salt, 1000)
    return hmac.compare_digest(password_hash, other_password)


if __name__ == "__main__":
    _pwd_hash: str = "80309097b712c6828d0f3f6dfd713e80"
    _other_password: str = "H4RDP4S$w0rd"
    print(easy(_pwd_hash, _other_password))

    _password_hash: bytes = b'\xb6`^\x81q\xd8e\x0b\x1f\x93YR\x8dE\x0c\x0f\xc2\xe4\xbc\x14\xf5\xdf\xdc\xec\xad\xcf\xf3\xca\xd2C\x17\xbb'
    _other_password: str = 'H4RDP4S$w0rd'
    _salt: str = 'Skypro'
    _algo: str = 'SHA256'
    print(hard(_password_hash, _other_password, _salt, _algo))

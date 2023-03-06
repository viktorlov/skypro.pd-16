# А теперь давайте проверим, правильный ли тип 
# данных возвращают тестируемые нами функции
# для этого нам поможет встроенная функция isinstance

# Давайте напишем еще 2 теста 
# для каждой функции и посмотрим на самом ли деле 
# при ошибках возвращаются строки, а при нормальной работе - целые числа
# Напишите 4 проверки в функции test_summer и 4 проверки в функции test_divider.
# Кстати, в одной тестовой функции можно написать больше одного assert

import os

def summer(*args):
    if len(args) == 1:
        return "Мало аргументов"
    for arg in args:
        if not isinstance(arg, int):
            return "ОШИБКА"
    if sum(args) > 300:
        return "Большое число"
    return sum(args)

def divider(a, b):
    for arg in [a, b]:
        if not isinstance(arg, int):
            return "ОШИБКА"
    if b == 0:
        return "Делить на ноль нельзя"
    return a / b


def test_summer():
    # TODO Напишите Ваши тесты здесь
    pass

def test_divider():
    # TODO Напишите Ваши тесты здесь
    pass


# Имитируем команду pytest при запуске модуля
if __name__ == "__main__":
    os.system("pytest")

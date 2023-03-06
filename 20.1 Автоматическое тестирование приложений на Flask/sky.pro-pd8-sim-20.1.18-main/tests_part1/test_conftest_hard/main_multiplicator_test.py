# фаил c тестами № 2
# Основной текст задания находится в файле main_summer_test.py
#
import os
from functools import reduce


# Исходная функция:
def multiplicator(*args):
    return reduce(lambda x, y: x * y, args)


def test_multiplicator(list_creator):
    # TODO напишите тест здесь
    assert multiplicator(*list_creator) == 57456000

if __name__ == "__main__":
    os.system("pytest -s")
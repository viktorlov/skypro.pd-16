from task import *


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_coffee = Coffee(title='Кофе', units='г.', quantity=5)
test2_coffee = Coffee(title='Много кофе')

test_assert(all((test_coffee.units == 'г.', test2_coffee.units == 'л.')), correct='Затенение units реализовано верно',
            incorrect='Затенение units реализовано НЕ верно')

test_assert(all((test_coffee.quantity == 5, test2_coffee.quantity == 3)),
            correct='Затенение quantity реализовано верно', incorrect='Затенение quantity реализовано НЕ верно')

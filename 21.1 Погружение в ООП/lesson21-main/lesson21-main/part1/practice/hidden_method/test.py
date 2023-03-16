from task import *

# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_disc = 0.8
test_discount = Discount()
test_discount.add_discount(title='котики', discount=test_disc)

test_item = Item(title='котики',
                 unit='шт.',
                 price_for_unit=100,
                 quantity=1,
                 discount=test_discount)
test_value = test_discount.check_discount(title='котики')

test_assert(test_value == test_disc, correct='Функции класса Discount реализованы верно',
            incorrect='Функции класса Discount реализованы НЕ верно')
test_assert(test_item.get_price() > 19.999 and test_item.get_price() <= 20,
            correct='Функиця "_calculate_discount" класса Item реализована верно',
            incorrect='Функиця "_calculate_discount" класса Item реализована НЕ верно')

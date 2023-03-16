from task import *


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_store = Store()
test_assert(hasattr(test_store, 'store'), correct='Атрибут store присутствует в классе Store',
            incorrect='Атрибут store отсутствует в классе Store')
test_assert(isinstance(test_store.store, dict), correct='Атрибут store верно реализован словарем',
            incorrect='Атрибут store должен быть реализован словарем')

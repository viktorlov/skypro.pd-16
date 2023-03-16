from task import *

# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


class TestGoods(Goods):
    total_quantity = 10


goods = TestGoods(qnt=1)
test_assert(goods._get_total() == 9, correct='Функция "_get_total" класса Goods реализована корректно',
            incorrect='Функция "_get_total" класса Goods реализована НЕ корректно')
goods._set_total(qnt=333)
test_assert(goods._get_total() == 333, correct='Функция "_set_total" класса Goods реализована корректно',
            incorrect='Функция "_set_total" класса Goods реализована НЕ корректно')

g0 = Goods(qnt=0)
g0._set_total(10)
g1 = Goods(qnt=5)
test_assert(g1.total_quantity == 5, correct='Функиця __init__ класса Goods реализована корректно #1',
            incorrect='Функиця __init__ класса Goods реализована НЕ корректно #1')
g2 = Goods(qnt=500)
test_assert(g1.total_quantity == 0, correct='Функиця __init__ класса Goods реализована корректно #2',
            incorrect='Функиця __init__ класса Goods реализована НЕ корректно #2')

ptn = Python(qnt=400)
ptn._set_total(qnt=333)
test_assert(ptn._get_total() == 333, correct='Класс Python реализован корректно',
            incorrect='Класс Python реализован НЕ корректно')

bk = Book(qnt=400)
bk._set_total(qnt=222)
test_assert(bk._get_total() == 222, correct='Класс Book реализован корректно',
            incorrect='Класс Book реализован НЕ корректно')

cof = Coffe(qnt=400)
cof._set_total(qnt=111)
test_assert(cof._get_total() == 111, correct='Класс Coffe реализован корректно',
            incorrect='Класс Coffe реализован НЕ корректно')

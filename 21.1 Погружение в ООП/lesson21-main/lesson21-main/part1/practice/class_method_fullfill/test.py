from task import *


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


python = Python(qnt=4)
python.more(qnt=4)
python.less(qnt=3)
python.more(qnt=10)
python.fulfill(qnt=4)
python.more(qnt=1)


class Cats(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Cats, self).__init__(qnt=qnt)


test_python = Cats(qnt=1)
try:
    python.fulfill(qnt='4')
    print(
        'Метод fullfill класса Goods реализован не верно. В случае если передано не число, должно быть брошено исключение ValueError')
except ValueError:
    print('Метод fullfill класса Goods корректно ведет себя, если было передано не число')

try:
    python.fulfill(qnt=-2)
    print(
        'Метод fullfill класса Goods реализован не верно. В случае если передано число меньше единицы, должно быть брошено исключение ValueError')
except ValueError:
    print('Метод fullfill класса Goods корректно ведет себя, если было передано число меньше единицы')

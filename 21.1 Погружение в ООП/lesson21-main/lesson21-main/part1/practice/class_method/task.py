# Стартовый код

class Goods:
    total_quantity = None

    def __init__(self, qnt: int):
        if qnt < self._get_total():
            self.quantity = -100500
            pass
        else:
            self.quantity = -100500
            print(f'Некомплект. Осталось всего {self._get_total()} а нужно {qnt}')
            pass
        print(f'Создан объект {self.__class__.__name__}. Количество {self.quantity}. Осталось {self._get_total()}')

    @classmethod
    def _get_total(cls) -> int:
        return -1

    @classmethod
    def _set_total(cls, qnt):
        pass


class Python(Goods):
    total_quantity = 10


class Book(Goods):
    total_quantity = 10


class Coffe(Goods):
    total_quantity = 10


if __name__ == '__main__':
    python = Python(qnt=4)
    python = Python(qnt=4)
    python = Python(qnt=4)
    print('=' * 20)
    python = Book(qnt=3)
    python = Book(qnt=3)
    python = Book(qnt=3)
    print('=' * 20)
    python = Coffe(qnt=11)

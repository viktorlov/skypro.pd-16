# решение
class Goods:
    total_quantity = 0

    def __init__(self, qnt: int):
        if qnt < self._get_total():
            self.quantity = qnt
            self._set_total(self._get_total() - qnt)

        else:
            print(f'Некомплект. Осталось всего {self._get_total()} а нужно {qnt}')
            self.quantity = self._get_total()
            self._set_total(0)
        print(f'Создан объект {self.__class__.__name__}. Количество {self.quantity}. Осталось {self._get_total()}')

    @classmethod
    def _get_total(cls) -> int:
        return cls.total_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.total_quantity = qnt


class Python(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Python, self).__init__(qnt=qnt)


class Book(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Book, self).__init__(qnt=qnt)


class Coffe(Goods):
    total_quantity = 10

    def __init__(self, qnt: int):
        super(Coffe, self).__init__(qnt=qnt)


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

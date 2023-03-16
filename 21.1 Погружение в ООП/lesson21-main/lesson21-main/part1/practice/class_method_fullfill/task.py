# Стартовый код
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

    def more(self, qnt: int):
        if self._get_total() == 0:
            return False
        if self._get_total() < qnt:
            qnt = self._get_total()
        self._set_total(self._get_total() - qnt)
        self.quantity += qnt
        self._report()

    def less(self, qnt: int):
        if self.quantity < qnt:
            qnt = self.quantity
        self._set_total(self._get_total() + qnt)
        self.quantity -= qnt
        self._report()

    def fulfill(self, qnt: int):
        pass

    def _report(self):
        print(f'Теперь у объекта {self.__class__.__name__} {self.quantity} единиц. На складе {self._get_total()}')

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


if __name__ == '__main__':
    python = Python(qnt=4)
    python.more(qnt=4)
    python.less(qnt=3)
    python.more(qnt=10)
    python.fulfill(qnt=4)
    python.more(qnt=1)

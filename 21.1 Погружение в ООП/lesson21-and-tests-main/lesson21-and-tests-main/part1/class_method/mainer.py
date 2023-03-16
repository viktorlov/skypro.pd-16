class GoodsQuantity:

    def __init__(self, goods_quantity=10):
        self._goods_quantity = goods_quantity

    def value(self):
        return self._goods_quantity


class Storage:
    goods_quantity = GoodsQuantity().value()

    def __init__(self, qnt):
        total = Storage._get_total()
        self.goods_quantity = qnt if qnt <= total else total
        Storage._set_total(total - self.goods_quantity)

    @classmethod
    def _get_total(cls):
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt


# Как закончите писать код, запустите его, 
# чтобы проверить работоспособность
# своего склада
if __name__ == '__main__':
    # goods_quantity = 10
    print("Всего на складе: ", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 4 ед. со склада)")
    python = Storage(qnt=4)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 5 ед. со склада)")
    python = Storage(qnt=5)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 2 ед. со склада)")
    python = Storage(qnt=2)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.goods_quantity)
    print('=' * 20)

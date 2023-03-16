# Продолжите прошлое задание, реализуйте
# метод fulfill, который 
# бы полностью отгружал все имеющиеся товары
# со склада (класса) в экземпляр класса.
# Попробуйте поэкспериментировать с кодом в блоке if __name__ == __main__

class GoodsQuantity:

    def __init__(self, goods_quantity=10):
        self._goods_quantity = goods_quantity

    def value(self):
        return self._goods_quantity


class Storage:
    goods_quantity = GoodsQuantity(15).value()

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

    def more(self, qnt):
        total = self._get_total()
        qnt = qnt if qnt <= total else total
        self.goods_quantity += qnt
        self._set_total(total - qnt)

    def less(self, qnt):
        total = self.goods_quantity
        qnt = qnt if qnt <= total else total
        self.goods_quantity -= qnt
        self._set_total(self._get_total() + qnt)

    def fullfill(self):
        self.goods_quantity += self._get_total()
        self._set_total(0)


# Посмотрите, что происходит с классом при применении различных методов.
# Можете поэкспериментировать и попробовать добавить свои.
if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 4 ед. со склада)")
    python = Storage(qnt=4)
    print("Осталось на складе: ", Storage.goods_quantity)
    print("Отгрузили со склада в экземпляр класса:", python.goods_quantity)
    print("Отгружаем все имеющиеся товары со склада в экземпляр класса:")
    python.fullfill()
    print("Осталось на складе:", Storage.goods_quantity)
    print("Имеется в экземпляре:", python.goods_quantity)

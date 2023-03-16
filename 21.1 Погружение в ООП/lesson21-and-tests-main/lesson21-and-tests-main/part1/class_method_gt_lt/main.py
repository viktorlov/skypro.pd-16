# Продолжите прошлое задание, но добавьте методы more, less.
# - Метод more у объекта увеличивает количество товара в экземпляре класса
#   на заданное число и одновременно с этим уменьшает 
#   число товаров на складе на это же число.
# - Метод less у объекта уменьшает количество товара в экземпляре класса на
#   заданное число, одновременно с этим увеличивает число 
#   товара на складе на это же число


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


if __name__ == '__main__':
    print("Всего на складе: ", Storage.goods_quantity)
    print("Создаём экземпляр класса Goods (пытаемся забрать 6 ед. со склада)")
    storage = Storage(6)
    print("Отгружаем 5 ед. товара со склада в экземпляр класса")
    storage.more(5)
    print("Число отгруженных товаров возросло до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.less(4)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)
    storage.less(8)
    print("Число отгруженных товаров сократилось до:", storage.goods_quantity)
    print("Остаток на складе: ", Storage.goods_quantity)

class Storage:
    goods_quantity = 10

    def __init__(self, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity = qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @classmethod
    def _get_total(cls):
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt
    
    def more(self, qnt):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity += qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)
    
    def less(self, qnt):
        if qnt < self.goods_quantity:
            self.goods_quantity = (self.goods_quantity - qnt)
            self._set_total(self._get_total() + qnt)
        else:
            self._set_total(self._get_total() + self.goods_quantity)
            self.goods_quantity = 0

    def fullfill(self):
        self.goods_quantity = self.goods_quantity + self._get_total()
        self._set_total(0)
# Решение
class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity

    def total_price(self) -> float:
        price = float(self.price_for_unit * self.quantity)
        return price

    def __repr__(self):
        return f'{self.title}, {self.unit}, {self.quantity}{self.unit}, {self.total_price()} руб.'

    def __eq__(self, other):
        return self.total_price() == other.total_price()

    def __ne__(self, other):
        return self.total_price() != other.total_price()

    def __gt__(self, other):
        return self.total_price() > other.total_price()

    def __ge__(self, other):
        return self.total_price() >= other.total_price()

    def __lt__(self, other):
        return self.total_price() < other.total_price()

    def __le__(self, other):
        return self.total_price() <= other.total_price()

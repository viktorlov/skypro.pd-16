class Item:
    def __init__(self, title, price, unit, quantity, discount_value=None):
        self.title = title
        self.price = price
        self.unit = unit
        self.quantity = quantity
        self.discount_value = discount_value

    def total_price(self):
        if self.discount_value:
            return self._calculate_discount()
        return self.price * self.quantity

    def _calculate_discount(self):
        return self.price * self.quantity * (1 - self.discount_value) 

class Cheque:
    def __init__(self):
        self.items = []

    def add_item(self, title, price, unit, quantity, discount_value=None):
        item = Item(title=title, price=price, unit=unit, quantity=quantity, discount_value=discount_value)
        self.items.append(item)

    def purchases(self):
        return "\n".join(
            [f"{item.title}, {item.quantity} {item.unit} - {item.total_price()}" for item in self.items])
    
    def get_sum(self):
        cheque_sum = sum([item.total_price() for item in self.items])
        return f"Сумма: {cheque_sum}"
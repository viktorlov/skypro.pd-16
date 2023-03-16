class Item:
    def __init__(self, title, price, unit, quantity):
        self.title = title
        self.price = price
        self.unit = unit
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Cheque:
    def __init__(self):
        self.items = []

    def add_item(self, title, price, unit, quantity):
        item = Item(title=title, price=price, unit=unit, quantity=quantity)
        self.items.append(item)

    def purchases(self):
        return "\n".join(
            [f"{item.title}, {item.quantity}{item.unit} - {item.total_price()}" for item in self.items])
    
    def get_sum(self):
        cheque_sum = sum([item.total_price() for item in self.items])
        return f"Сумма: {cheque_sum}"

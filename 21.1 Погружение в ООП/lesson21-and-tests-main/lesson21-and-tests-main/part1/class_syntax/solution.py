class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Cheque:
    def __init__(self):
        self.items = []

    def purchases(self):
        return "\n".join([f"{item.title} - {item.price}" for item in self.items])
    
    def get_sum(self):
        cheque_sum = sum([item.price for item in self.items])
        return f"Всего: {cheque_sum}"
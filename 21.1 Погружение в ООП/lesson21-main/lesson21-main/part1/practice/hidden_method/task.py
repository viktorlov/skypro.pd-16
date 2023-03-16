# Стартовый код
class Company:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone


class Discount:
    def __init__(self):
        self.discounts = {}

    def add_discount(self, title: str, discount: float):
        pass

    def check_discount(self, title: str) -> float:
        pass


class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float, discount: Discount):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity
        self.discount = discount

    def get_price(self) -> float:
        price = float(self.price_for_unit * self.quantity)
        return self._calculate_discount(price)

    def _calculate_discount(self, price: float):
        pass


class Receipt:
    def __init__(self):
        self.company = None
        self.items = []
        self.discount = Discount()

    def set_company(self, company: Company):
        self.company = company

    def set_discount(self, discount: Discount):
        self.discount = discount

    def add_item(self, title: str, unit: str, price_for_unit: float, quantity: float):
        item = Item(title=title,
                    unit=unit,
                    price_for_unit=price_for_unit,
                    quantity=quantity,
                    discount=self.discount)
        self.items.append(item)

    def print(self):
        total_price = 0

        for item in self.items:
            title_with_unit = f'{item.title}, {item.unit}'
            print(f'{title_with_unit} - {item.quantity} - {item.get_price()}')
            total_price += item.get_price()
        print(f'Всего: {total_price}')

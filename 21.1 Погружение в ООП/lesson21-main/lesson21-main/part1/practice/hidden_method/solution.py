# Решение

class Company:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone


class Discount:
    def __init__(self):
        self.discounts = {}

    def add_discount(self, title: str, discount: float):
        self.discounts[title] = discount

    def check_discount(self, title: str) -> float:
        if title in self.discounts:
            return self.discounts[title]
        return 0.0


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
        discount = self.discount.check_discount(title=self.title)
        return price * (1 - discount)


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


if __name__ == '__main__':
    company = Company(name='ООО Классные Объекты',
                      address='г. Город, ул. Улица, д 13',
                      phone='12345678')
    discount = Discount()
    discount.add_discount(title='Сушеные питоны', discount=0.1)
    discount.add_discount(title='Книги про PHP', discount=-0.1)
    receipt = Receipt()
    receipt.set_company(company=company)
    receipt.set_discount(discount=discount)
    receipt.add_item(title='Сушеные питоны', unit='упаковка.',
                     price_for_unit=100, quantity=5)
    receipt.add_item(title='Книги про PHP', unit='шт.',
                     price_for_unit=1, quantity=10)
    receipt.add_item(title='Кофе плохорастворенный', unit='л.',
                     price_for_unit=1000, quantity=.2)
    receipt.print()

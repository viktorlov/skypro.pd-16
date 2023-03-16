# Стартовый код

class Company:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone


class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float):
        pass

    def get_price(self) -> float:
        pass


class Receipt:
    def __init__(self):
        self.company = None
        self.items = []

    def set_company(self, company: Company):
        pass

    def add_item(self, title: str, unit: str, price_for_unit: float, quantity: float):
        pass

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
    
    receipt = Receipt()
    receipt.set_company(company=company)
    receipt.add_item(title='Сушеные питоны', unit='упаковка.',
                     price_for_unit=100, quantity=5)
    receipt.add_item(title='Книги про PHP', unit='шт.',
                     price_for_unit=1, quantity=10)
    receipt.add_item(title='Кофе плохорастворенный', unit='л.',
                     price_for_unit=1000, quantity=.2)
    receipt.print()
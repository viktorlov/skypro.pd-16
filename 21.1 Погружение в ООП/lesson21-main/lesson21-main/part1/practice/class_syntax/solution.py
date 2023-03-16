# Решение

class Item:
    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price


class Company:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone


class Receipt:
    def __init__(self):
        self.company = None
        self.items = []

    def print(self):
        total_price = 0
        for item in self.items:
            print(f'{item.title} - {item.price}')
            total_price += item.price
        print(f'Всего: {total_price}')

if __name__ == '__main__':
    
    
    company = Company(name='ООО Классные Объекты',
                      address='г. Город, ул. Улица, д 13',
                      phone='12345678')
    
    dry_pythons = Item(title='Сушеные питоны, упаковка', price=500)
    php_books = Item(title='Книги про PHP, шт', price=10)
    questionable_coffe = Item(title='Кофе плохорастворенный, шт', price=200)
    
    receipt = Receipt()
    receipt.company = company
    receipt.items.extend([dry_pythons, php_books, questionable_coffe])
    receipt.print()
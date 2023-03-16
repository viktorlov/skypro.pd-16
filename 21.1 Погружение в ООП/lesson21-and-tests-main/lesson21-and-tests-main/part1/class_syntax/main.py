#  Реализуйте класс товара (Item) с аттрибутами:
#   - название(title)
#   - цена(price)
# 
#  Реализуйте класс чек (Cheque) который должен содержать:
#   Аттрибут items (должен представлять собой список).
#   (В блоке if __name__ == "__main__" мы добавим туда покупки).
#
# Метод purchases, который должен вернуть строку вида:
#   Сушеные питоны - 500
#   Книги про PHP - 10
#   Кофе плохорастворенный - 200
#
# Метод get_sum, который должен вернуть строку вида:
#   Всего: 710

from functools import reduce


class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"{self.title} - {self.price}"


class Cheque:
    def __init__(self):
        self.items = []

    def purchases(self):
        return "\n".join([str(item) for item in self.items])

    def get_sum(self):
        return f"Всего: {reduce(lambda total, item: total + item.price, self.items, 0)}"


if __name__ == '__main__':
    # Создаём товары с ценой
    dry_pythons = Item(title='Сушеные питоны', price=500)
    php_books = Item(title='Книги про PHP', price=700)
    questionable_coffe = Item(title='Кофе плохорастворенный', price=200)
    # Создаём чек
    cheque = Cheque()
    # Добавляем товары в чек
    cheque.items.extend([dry_pythons, php_books, questionable_coffe])
    # Печатаем чек
    print(cheque.purchases())
    print(cheque.get_sum())

# Возьмем классы из прошлого задания и немного усовершенствуем их.
#
# Добавим в класс Item:
#   Аттрибут unit, который будет содержать единицу измерения.
#   Аттрибут quantity, который будет содержать количество ед. товара.
# Такие аттрибуты должны создаваться при инициализации класса.
#
# Добавим метод total_price, вызывая который мы получаем общую цену конкретных товаров.
# Например, при создании экземпляра класса Item(title=сахар, price=100, unit='кг', quantity=4)
# вызов метода total_price экземпляра класса Item должен возвращать 400.
# 
# Реализуйте метод add_item в классе Cheque, который будет создавать экземпляр класса
# Item и автоматически добавлять его в список items.
# Например: add_item("Кофе", "л", 300, 0.2)
#
#
# Немного усовершенствуем вывод список покупок, теперь он должен быть вида:
#   Сахар, 3.5кг - 350
#   Кофе, 0.2л - 60
#
# Функцию определяющую сумму покупок также необходимо будет доработать.
# Теперь, чтобы посчитать сумму всех покупок, необходимо использовать метод total_price.
# Формат вывода мы оставим прежний:
#   Сумма: 410

from functools import reduce


class Item:
    def __init__(self, title, price, unit, quantity):
        self.title = title
        self.price = price
        self.unit = unit
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.title}, {self.quantity}{self.unit} - {self.total_price()}"


class Cheque:
    def __init__(self):
        self.items = []

    def purchases(self):
        return "\n".join([str(item) for item in self.items])

    def get_sum(self):
        cheque_sum = reduce(lambda total, item: total + item.total_price(), self.items, 0)
        return f"Сумма: {cheque_sum}"

    def add_item(self, **kwargs):
        self.items.append(Item(**kwargs))


# Это проверочный код, запустите файл, чтобы увидеть логику работы классов
if __name__ == '__main__':
    # Создаём чек
    cheque = Cheque()
    # Добавляем товары в чек
    cheque.add_item(title='Сушеные питоны', price=500, unit='шт', quantity=5)
    cheque.add_item(title='Книги про PHP', price=700, unit='шт', quantity=3)
    cheque.add_item(title='Кофе плохорастворенный', price=200, unit='л', quantity=0.2)
    # Печатаем чек
    print(cheque.purchases())
    print(cheque.get_sum())

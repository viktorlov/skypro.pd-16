# Реализовать для объектов Item методы
# 1. Магический метод представления __repr__
#    возвращающий строковое представление объекта.
#    Будем ожидать что при вызове print(items) выведется строка вида: 
#    "Жареные питоны, 0.3 г, 150.0 руб." (В качестве цены здесь понимается стоимость товара с учетом его количества)
# 2. Магические методы, позволяющие сравнить между собой объекты по цене:
#    - __gt__
#    - __ge__
#    - __lt__
#    - __le__
#    - __eq__
#    - __ne__


class Item:
    def __init__(self, title, unit, price_for_unit, quantity):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity

    def total_price(self):
        price = float(self.price_for_unit * self.quantity)
        return price

    def __repr__(self):
        return f"{self.title}, {self.quantity} {self.unit}, {self.total_price()} руб."

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


# Здесь код для самопроверки, 
# если в терминале хотя бы один пункт ложь, тогда ищите ошибку в коде,
# А если совсем запутались, запустите наши тесты и мы подскажем
if __name__ == '__main__':
    dried_pythons = Item(
        title='Сушеные питоны',
        unit='г',
        price_for_unit=500,
        quantity=0.3)

    fried_pythons = Item(
        title='Жареные питоны',
        unit='г',
        price_for_unit=500,
        quantity=0.3)

    cooked_pythons = Item(
        title='Варёные питоны',
        unit='г',
        price_for_unit=700,
        quantity=0.3)


    def true_lie(assertion):
        if assertion:
            return "Правда"
        return "Ложь"


    print(fried_pythons)
    print(
        "Правда ли что сушеные и жареные питоны стоят одинаково?",
        true_lie(dried_pythons == fried_pythons))
    print(
        "Правда ли что сушеные и вареные питоны стоят по разному?",
        true_lie(dried_pythons != cooked_pythons))
    print(
        "Правда ли что вареные питоны стоят больше чем сушеные?",
        true_lie(cooked_pythons > dried_pythons)
    )
    print(
        "Правда ли что жареные питоны стоят меньше чем варёные?",
        true_lie(fried_pythons < cooked_pythons)
    )
    print(
        "Правда ли что жареные питоны по стоимости меньше или равны сушёным?",
        true_lie(fried_pythons <= dried_pythons)
    )
    print(
        "Правда ли что жареные питоны по стоимости меньше или равны варёным?",
        true_lie(fried_pythons <= cooked_pythons)
    )
    print(
        "Правда ли что жареные питоны по стоимости больше или равны сушёным?",
        true_lie(fried_pythons >= dried_pythons)
    )
    print(
        "Правда ли что варёные питоны по стоимости больше или равны жареным?",
        true_lie(cooked_pythons >= fried_pythons)
    )

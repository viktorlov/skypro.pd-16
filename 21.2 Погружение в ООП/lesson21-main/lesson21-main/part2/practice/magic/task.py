# Исходный код
class Item:
    def __init__(self, title: str, unit: str, price_for_unit: float, quantity: float):
        self.title = title
        self.unit = unit
        self.price_for_unit = price_for_unit
        self.quantity = quantity

    def get_price(self) -> float:
        price = float(self.price_for_unit * self.quantity)
        return price

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

if __name__ == '__main__':
        
    pythons = Item(title='Сушеные питоны',
                   unit='г.',
                   price_for_unit=1000,
                   quantity=0.3)
    
    pythons2 = Item(title='Сушеные питоны',
                    unit='г.',
                    price_for_unit=1000,
                    quantity=0.3)
    
    pythons3 = Item(title='Сушеные питоны',
                    unit='г.',
                    price_for_unit=1000,
                    quantity=0.4)
    
    print(pythons)  # Результат должен быть таким - Сушеные питоны, г., 0.3г., 300.0 руб.
    assert pythons == pythons2, 'Ошибка в реализации __eq__'
    assert pythons != pythons3, 'Ошибка в реализации __ne__'
    assert pythons3 > pythons2, 'Ошибка в реализации __gt__'
    assert pythons < pythons3, 'Ошибка в реализации __lt__'
    assert pythons >= pythons2, 'Ошибка в реализации __ge__'
    assert pythons <= pythons2, 'Ошибка в реализации __le__'

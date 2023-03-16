
# Решение
class Goods:
    units = 'л.'
    quantity = 3

    def __init__(self, title: str, **kwargs):
        self.title = title

    def prnt(self):
        print(f'{self.title} {self.quantity} {self.units}')


class Coffee(Goods):
    def __init__(self, **kwargs):
        super(Coffee, self).__init__(**kwargs)
        if 'units' in kwargs:
            self.units = kwargs['units']
        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']


class Water(Goods):
    def __init__(self, **kwargs):
        super(Water, self).__init__(**kwargs)
        if 'units' in kwargs:
            self.units = kwargs['units']
        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']


class Cookies(Goods):
    def __init__(self, **kwargs):
        super(Cookies, self).__init__(**kwargs)
        if 'units' in kwargs:
            self.units = kwargs['units']
        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

if __name__ == '__main__':
        
    my_coffee = Coffee(title='Кофе', units='г.', quantity=3)
    another_coffee = Coffee(title='Кофе', units='ведр.')
    my_water = Water(title='Вода', units='л.', quantity=4)
    another_water = Water(title='Вода', quantity=5)
    my_cookies = Cookies(title='Печеньки', units='уп.', quantity=1)
    
    my_coffee.prnt()
    my_water.prnt()
    my_cookies.prnt()
    another_water.prnt()
    another_coffee.prnt()


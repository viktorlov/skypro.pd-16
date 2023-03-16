print('cls - обращение к самому классу создавшему объект для вызова методов связанных со всеми созданными объектами.'
      ' На самом деле имена self или cls описаны в соглашении PEP8 но не являются обязательными, вы можете вместо них'
      ' использовать например свое имя... но тогда с чтением вашего кода у других программистов могут возникнуть '
      'сложности\n')


class Store:
    quantity = 10

    def __init__(self, name: str, qnt: int):
        self.name = name
        self.qnt = qnt

        Store.quantity -= self.qnt

        print(f"Взяли {qnt} со склада, осталось {self._class_qnt()}")

    def _class_qnt(self):
        return Store.quantity


order = Store(name='Заказ 1', qnt=2)
order2 = Store(name='Заказ 2', qnt=3)

print('\nОбратите внимание, что не смотря на то, что метод _class_qnt вызывается через self работает он с переменной'
      ' класса quantity. То же самое можно записать немного по другому\n')


class Store:
    quantity = 10

    def __init__(self, name: str, qnt: int):
        self.name = name
        self.qnt = qnt

        Store.quantity -= self.qnt

        print(f"Взяли {qnt} со склада, осталось {self._class_qnt()}")
        # Или даже можно так
        # print(f"Взяли {qnt} со склада, осталось {Store._class_qnt()}")

    @classmethod
    def _class_qnt(cls):
        return cls.quantity


def sabotage(*args, **kwargs):
    return 'саботаж'


order = Store(name='Заказ 1', qnt=2)
order2 = Store(name='Заказ 2', qnt=3)
print(order2._class_qnt())
print('\nОбратите внимание что через объект получить доступ к методу класса для его подмены все равно не выйдет\n')
order2._class_qnt = sabotage
print(order2._class_qnt())

order3 = Store(name='Заказ 3', qnt=1)
print('\nА вот подмена в самом классе пройдет успешно\n')
Store._class_qnt = sabotage
order3 = Store(name='Заказ 4', qnt=3)

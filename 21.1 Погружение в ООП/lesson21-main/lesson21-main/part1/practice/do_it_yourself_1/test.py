from task import *


# Тесты и код проверки
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert('Unit' in globals(), correct='Класс Unit успешно создан',
            incorrect='Методы должны быть помещены в класс по имени Unit')
unit = Unit(name='Опытный тыловик', hp=10, defense=1, power=1, x_coord=1, y_coord=1)
test_assert(hasattr(unit, 'name'), correct='У класса Unit есть атрибут "name"',
            incorrect='У класса Unit отсутствует атрибут "name"')
test_assert(hasattr(unit, 'hp'), correct='У класса Unit есть атрибут "hp"',
            incorrect='У класса Unit отсутствует атрибут "hp"')
test_assert(hasattr(unit, 'defense'), correct='У класса Unit есть атрибут "defense"',
            incorrect='У класса Unit отсутствует атрибут "defense"')
test_assert(hasattr(unit, 'power'), correct='У класса Unit есть атрибут "power"',
            incorrect='У класса Unit отсутствует атрибут "power"')
test_assert(hasattr(unit, 'x'), correct='У класса Unit есть атрибут "x"',
            incorrect='У класса Unit отсутствует атрибут "x"')
test_assert(hasattr(unit, 'y'), correct='У класса Unit есть атрибут "y"',
            incorrect='У класса Unit отсутствует атрибут "y"')
unit.move_up()
unit.move_up()
test_assert(unit.y == 3, 'Функция "move_up" реализована корректно',
            incorrect='Функция "move_up" реализована НЕ корректно')
unit.move_down()
test_assert(unit.y == 2, 'Функция "move_down" реализована корректно',
            incorrect='Функция "move_down" реализована НЕ корректно')
unit.move_left()
test_assert(unit.x == 0, 'Функция "move_left" реализована корректно',
            incorrect='Функция "move_left" реализована НЕ корректно')
unit.move_right()
unit.move_right()
test_assert(unit.x == 2, 'Функция "move_right" реализована корректно',
            incorrect='Функция "move_right" реализована НЕ корректно')
test_unit = Unit(name='Опытный тыловик 2', hp=10, defense=1, power=1, x_coord=1, y_coord=1)
try:
    test_unit.get_damage(damage=11)
    print('Функция get_damage НЕ корректно отрабатывает 0 хп у юнита')
except UnitDied:
    print('Функция get_damage корректно отрабатывает 0 хп у юнита')

test_unit = Unit(name='Опытный тыловик 2', hp=10, defense=4, power=1, x_coord=1, y_coord=1)
test_unit.get_damage(damage=4)
test_assert(test_unit.hp == 10, correct='Защита юнита работает корректно',
            incorrect="Защита юнита работает НЕ корректно")

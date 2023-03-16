# Стартвый код

class UnitDied(Exception):
    pass


unit = {
    'name': 'Василий',
    'hp': 10,
    'defense': 1,
    'power': 2,
    'x': 1,
    'y': 1}


def move_unit_up(unit: dict):
    unit['y'] += 1


def move_unit_down(unit: dict):
    unit['y'] -= 1


def move_unit_right(unit: dict):
    unit['x'] += 1


def move_unit_left(unit: dict):
    unit['x'] -= 1


def hit_other_unit(unit: dict, other: dict):
    hit_power = unit['power']
    other_defense = other['defense']
    other['hp'] -= hit_power - other_defense


def get_damage_from_other_unit(unit: dict, other: dict):
    hit_other_unit(unit=other, other=unit)


def check_is_alive(unit: dict):
    if unit['hp'] <= 0:
        raise UnitDied


class Unit:
    def __init__(self, name: str, hp: int, defense: int, power: int, x_coord: int, y_coord: int):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def hit(self, other):
        pass

    def get_damage(self, damage: int):
        pass

    def is_alive(self) -> bool:
        pass


# Данная схватка определенно должна заканчиваться победой Былинного богатыря.
# Код ниже изменять не нужно, его достаточно для того чтобы провести схватку.
unit1 = Unit(name='Басурманин заморский', hp=10, defense=2, power=6, x_coord=1, y_coord=1)
unit2 = Unit(name='Богатырь былинный', hp=30, defense=4, power=3, x_coord=1, y_coord=1)
try:
    while all((unit1.is_alive(), unit2.is_alive())):
        unit1.hit(unit2)
        unit2.hit(unit1)
except UnitDied as e:
    print(e.args[0])

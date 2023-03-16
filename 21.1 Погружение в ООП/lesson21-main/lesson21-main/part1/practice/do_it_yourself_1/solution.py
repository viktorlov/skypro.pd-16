# Решение
class UnitDied(Exception):
    pass


class Unit:
    def __init__(self, name: str, hp: int, defense: int, power: int, x_coord: int, y_coord: int):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.x = x_coord
        self.y = y_coord
        self.power = power

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def hit(self, other):
        other.get_damage(self.power)

    def get_damage(self, damage: int):
        self.hp -= (damage - self.defense)
        self.is_alive()

    def is_alive(self) -> bool:
        if self.hp <= 0:
            raise UnitDied(f'Трагически погиб в неравном бою {self.name}')
        return True


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

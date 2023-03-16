import random

class UnitDied(Exception):
    pass


class Unit:
    def __init__(self, name, hp, defence, power):
        self.name = name
        self.hp = hp
        self.defence = defence
        self.power = power

    def hit(self, other):
        damage = random.choice(range(1, self.power))
        other._get_damage(damage)
        return f"{self.name} ({self.hp}) наносит {damage} урона {other.name} ({other.hp})"

    def _get_damage(self, damage):
        if damage > self.defence:
            self.hp -= (damage - self.defence)
        self.is_alive()

    def is_alive(self):
        if self.hp <= 0:
            raise UnitDied(f'Трагически погиб в неравном бою {self.name}')
        return True

unit1 = Unit(name='Басурманин заморский', hp=10, defence=1, power=5)
unit2 = Unit(name='Богатырь былинный', hp=30, defence=2, power=3)
try:
    while all((unit1.is_alive(), unit2.is_alive())):
        print(unit1.hit(unit2))
        print(unit2.hit(unit1))
except UnitDied as e:
    print(e.args[0])

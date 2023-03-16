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

class StoneGuard(Unit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.was_attacked = False

    def _get_damage(self, damage):
        if not self.was_attacked:
            damage = 0
            self.was_attacked = True
            print(f"{self.name} блокирует урон")
        super()._get_damage(damage)

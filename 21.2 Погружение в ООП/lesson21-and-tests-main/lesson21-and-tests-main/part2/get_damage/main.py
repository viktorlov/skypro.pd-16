# Давайте попробуем добавить нашим классам героя
# уникальные способности!
#
# Для этого воспользуемся возможностями наследования в ООП.
# Введем новый класс героя `StoneGuard`, у которого урон 
# от первой атаки игнорируется. 
#
# Реализуйте класс StoneGuard унаследовав от класса Unit.
# Переопределите метод _get_damage.
# Фиксируйте атаку с помощью поля (флага) was_attacked (можно использовать тип boolean)


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
    def __init__(self, name, hp, defence, power):
        super(StoneGuard, self).__init__(name, hp, defence, power)
        self.was_attacked = False

    def _get_damage(self, damage):
        if self.was_attacked:
            super(StoneGuard, self)._get_damage(damage)
            return
        print(f"{self.name} блокирует урон")
        self.was_attacked = True


# Логика кода ниже такая же, как и в предыдущем задании.
# Если вдруг интересно, то можно
# поэкспериментировать со значениями моделей
# Если вдруг схватка затянется, прервите её с помощью
# сочетания клавиш ctrl+c
if __name__ == '__main__':
    unit1 = StoneGuard(name='Каменный страж', hp=10, defence=2, power=5)
    unit2 = Unit(name='Богатырь былинный', hp=30, defence=2, power=4)
    try:
        while all((unit1.is_alive(), unit2.is_alive())):
            print(unit1.hit(unit2))
            print(unit2.hit(unit1))
    except UnitDied as e:
        print(e.args[0])

# Придумаем еще одного героя со способностью ярость (fury)
#
# Введем новый класс героя `FuriousHero`, у которого увеличивается атака на 1 ед.,
# каждый раз, когда герой получает урон. При этом, его атака не увеличивается если урон
# меньше, чем защита нашего нового героя.
#
# Реализуйте класс героя FuriousHero, унаследовав от класса Unit,
# и переопределить метод _get_damage.
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


class FuriousHero(Unit):
    def _get_damage(self, damage):
        last_hp = self.hp
        super(FuriousHero, self)._get_damage(damage)
        if self.hp < last_hp:
            self.power += 1


# Логика кода ниже такая же, как и в предыдущем задании.
# Если вдруг интересно, то можно
# поэксперементировать со значениями моделей
# Если вдруг схватка затянется, прервите её с помощью
# сочетания клавиш ctrl+с
if __name__ == "__main__":
    unit1 = Unit(name='Басурманин заморский', hp=20, defence=1, power=4)
    unit2 = FuriousHero(name='Яростный богатырь', hp=25, defence=2, power=2)
    try:
        while all((unit1.is_alive(), unit2.is_alive())):
            print(unit1.hit(unit2))
            print(unit2.hit(unit1))
    except UnitDied as e:
        print(e.args[0])

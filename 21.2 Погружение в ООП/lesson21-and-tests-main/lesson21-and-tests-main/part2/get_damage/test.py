import sys
import unittest
from pathlib import Path
import os
from main import Unit, UnitDied, StoneGuard
import inspect

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

class UnitTestCase(SkyproTestCase):
    
    @classmethod
    def setUpClass(self):
        self.stone = StoneGuard(name='Басурманин заморский', hp=20, defence=0, power=5)
        self.unit_2 = Unit(name='Богатырь былинный', hp=20, defence=0, power=3)

    def test_init_returns_class_instances(self):
        item_attrs = ['name', 'hp', 'defence', 'power', 'was_attacked']
        for attr in item_attrs:
            self.assertTrue(
                hasattr(self.stone, attr),
                f'%@Проверьте, что экземпляр класса StoneGuard имеет аттрибут {attr} '
                "(Проверяем метод __init__)"
            )
        self.unit_2._get_damage(5)
        self.assertFalse(
            self.unit_2.hp == 20,
            "%@Проверьте, что функция _get_damage работает корректно (юнит получает урон)"
        )
        
        self.unit_2.hit(self.stone)
        self.assertFalse(
            self.stone.hp != 20,
            "%@Проверьте что при нанесении удара по StoneGuard (он блокирует первый удар)"
        )
        self.unit_2.hit(self.stone)
        self.assertFalse(
            self.stone.hp == 20,
            "%@Проверьте что при нанесении удара по StoneGuard второй удар не блокируется"
        )


        self.stone.hp = 1
        self.unit_2.power = 100
        with self.assertRaises(UnitDied, msg="%@Проверьте что если уровень здоровье юнита меньше нуля, то StoneGuard погибает"):
            self.unit_2.hit(self.stone)

        code = inspect.getsource(StoneGuard.__init__)
        self.assertIn(
            'super', code,
            "%@На первый взгляд задача решена верно, однако мы всё же настаиваем на том"
            "чтобы в методе __init__ была использована функция super()"
        )

        code = inspect.getsource(StoneGuard._get_damage)
        self.assertIn(
            'super', code,
            "%@На первый взгляд задача решена верно, однако мы всё же настаиваем на том"
            "чтобы в методе _get_damage была использована функция super()"
        )

if __name__ == "__main__":
    unittest.main()

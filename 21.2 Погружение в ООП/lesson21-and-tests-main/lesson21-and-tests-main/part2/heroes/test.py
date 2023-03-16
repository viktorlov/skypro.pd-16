import sys
import unittest
from pathlib import Path
import os
from main import Unit, UnitDied

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
        self.unit_1 = Unit(name='Басурманин заморский', hp=20, defence=0, power=5)
        self.unit_2 = Unit(name='Богатырь былинный', hp=20, defence=0, power=3)

    def test_init_returns_class_instances(self):
        item_attrs = ['name', 'hp', 'defence', 'power']
        for attr in item_attrs:
            self.assertTrue(
                hasattr(self.unit_1, attr),
                f'%@Проверьте, что экземпляр класса Item имеет аттрибут {attr} '
                "(Проверяем метод __init__)"
            )
        self.unit_2._get_damage(5)
        self.assertFalse(
            self.unit_2.hp == 20,
            "%@Проверьте, что функция _get_damage работает корректно (юнит получает урон)"
        )
        
        self.unit_2.hit(self.unit_1)
        self.assertFalse(
            self.unit_1.hp == 20,
            "%@Проверьте что функция hit работает корректно (один юнит наносит удар а второй получает урон)"
        )
        self.unit_2.hp = 1
        self.unit_1.power = 100
        with self.assertRaises(UnitDied, msg="%@Проверьте что если уровень здоровье юнита меньше нуля, тогда он погибает"):
            self.unit_1.hit(self.unit_2)


if __name__ == "__main__":
    unittest.main()

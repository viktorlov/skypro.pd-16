import sys
import unittest
from pathlib import Path
import os
from main import FuriousHero, Unit, UnitDied
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
        self.furious = FuriousHero(name='Басурманин заморский', hp=20, defence=0, power=5)
        self.unit_2 = Unit(name='Богатырь былинный', hp=20, defence=0, power=3)

    def test_init_returns_class_instances(self):
        item_attrs = ['name', 'hp', 'defence', 'power']
        for attr in item_attrs:
            self.assertTrue(
                hasattr(self.furious, attr),
                f'%@Проверьте, что экземпляр класса Item имеет аттрибут {attr} '
                "(Проверяем метод __init__)"
            )
        self.unit_2._get_damage(5)
        self.assertFalse(
            self.unit_2.hp == 20,
            "%@Проверьте, что функция _get_damage работает корректно (юнит получает урон)"
        )
        
        self.unit_2.hit(self.furious)
        self.assertFalse(
            self.furious.hp == 20,
            "%@Проверьте что функция hit работает корректно (один юнит наносит удар а второй получает урон)"
        )

        hero_dmg = self.furious.power
        self.unit_2.hit(self.furious)
        self.assertTrue(
            self.furious.power == hero_dmg + 1,
            "%@Проверьте что после удара по яростному герою его сила увеличивается на 1 ед."
        )
        self.unit_2.hp = 1
        self.furious.power = 100
        with self.assertRaises(UnitDied, msg="%@Проверьте что если уровень здоровье юнита меньше нуля, тогда он погибает"):
            self.furious.hit(self.unit_2)

        code = inspect.getsource(FuriousHero._get_damage)
        self.assertIn(
            'super', code,
            "%@На первый взгляд задача решена верно, однако мы всё же настаиваем на том, "
            "чтобы в методе _get_damage была использована функция super()"
        )

if __name__ == "__main__":
    unittest.main()

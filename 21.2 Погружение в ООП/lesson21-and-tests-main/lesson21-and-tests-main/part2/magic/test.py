import sys
import unittest
from pathlib import Path
import os
from main import Item

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class CheckClassesTestCase(SkyproTestCase):
    
    @classmethod
    def setUpClass(self):
        self.dried_pythons = Item(
            title='Сушеные питоны',
            unit='г.',
            price_for_unit=500,
            quantity=0.3)
        
        self.fried_pythons = Item(
            title='Жареные питоны',
            unit='г.',
            price_for_unit=500,
            quantity=0.3)
        
        self.cooked_pythons = Item(
            title='Варёные питоны',
            unit='г.',
            price_for_unit=700,
            quantity=0.3)       

    def test_classes_attrs(self):

        self.assertTrue(
            self.dried_pythons == self.fried_pythons,
            "%@Проверьте, корректно ли реализован метод __eq__"
        )

        self.assertTrue(
            self.dried_pythons != self.cooked_pythons,
            "%@Проверьте, корректно ли реализован метод __ne__"
        )

        self.assertTrue(
            self.cooked_pythons > self.dried_pythons,
            "%@Проверьте, корректно ли реализован метод __gt__"
        )

        self.assertTrue(
            self.fried_pythons < self.cooked_pythons,
            "%@Проверьте, корректно ли реализован метод __lt__"
        )

        self.assertTrue(
            self.fried_pythons <= self.dried_pythons,
            "%@Проверьте, корректно ли реализован метод __le__"
        )

        self.assertTrue(
            self.fried_pythons <= self.cooked_pythons,
            "%@Проверьте, корректно ли реализован метод __le__"
        )

        self.assertTrue(
            self.fried_pythons >= self.dried_pythons,
            "%@Проверьте, корректно ли реализован метод __ge__"
        )

        self.assertTrue(
            self.cooked_pythons >= self.fried_pythons,
            "%@Проверьте, корректно ли реализован метод __ge__"
        )

        self.assertTrue(
            self.fried_pythons.__repr__() == 'Жареные питоны, 0.3 г., 150.0 руб.',
            "%@Проверьте, корректно ли реализован метод __repr__"
        )

if __name__ == "__main__":
    unittest.main()


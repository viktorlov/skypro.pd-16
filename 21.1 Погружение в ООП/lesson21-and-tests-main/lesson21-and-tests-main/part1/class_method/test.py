import sys
import unittest
from pathlib import Path
import os
from main import Storage

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

class ClassesTestCase(SkyproTestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.storage = Storage
        cls.storage.goods_quantity = 14
        

    def test_get_total_method(self):
        self.assertTrue(
            self.storage._get_total() == 14,
            "%@Проверьте, что внутренний метод класса _get_total возвращает "
            " количество находящихся товаров на складе")

    def test_init_method(self):
        self.storage._set_total(5)
        self.assertTrue(
            self.storage.goods_quantity == 5,
            "%@Проверьте, что внутренний метод класса _set_total присваивает "
            "новое значение переменной класса `goods_quantity")
        instance = self.storage(3)
        self.assertTrue(
            self.storage._get_total() == 2,
            "%@Проверьте, что при инициализации экземпляра класса количество "
            "находящихся на складе товаров уменьшается корректно")

        self.assertTrue(
            hasattr(instance, 'goods_quantity'),
            "%@Проверьте что экземпляр класса после инициализации имеет свойство "
            "goods_quantity")

        self.assertTrue(
            instance.goods_quantity == 3,
            "%@Проверьте что свойству `goods_quantity` экземпляра класса при инициализации "
            "присваивается правильное значение"
            )

if __name__ == "__main__":
    unittest.main()
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
        self.storage._set_total(20)

        instance.more(4)
        self.assertTrue(
            instance.goods_quantity == 7,
            "%@Проверьте что при применении к экземпляру класса метода more, его аттрибут "
            "goods_quantity увеличивается"
        )

        self.assertTrue(
            self.storage._get_total() == 16,
            "%@Проверьте что при применении к экземпляру класса метода more, на складе "
            "число товаров уменьшается"
        )

        instance.less(6)
        self.assertTrue(
            instance.goods_quantity == 1,
            "%@Проверьте что при применении к экземпляру класса метода less, его аттрибут "
            "goods_quantity уменьшается"
        )

        self.assertTrue(
            self.storage._get_total() == 22,
            "%@Проверьте что при применении к экземпляру класса метода less, на складе "
            "число товаров увеличивается"
        )

        instance.less(2)
        self.assertTrue(
            instance.goods_quantity == 0,
            "%@Проверьте что если к экземпляру класса применен метод less а товаров "
            "недостаточно, тогда их число не становится меньше нуля"
        )

        self.assertTrue(
            self.storage._get_total() == 23,
            "%@Проверьте что если к экземпляру класса применен метод less а товаров "
            "недостаточно, то на складе не возникают лишние товары"
        )
        instance.more(24)
        self.assertTrue(
            self.storage._get_total() == 0,
            "%@Проверьте что если к экземпляру класса применен метод more а товаров "
            "на складе недостаточно, значение последних не становится ниже нуля"
        )

        self.assertTrue(
            instance.goods_quantity == 23,
            "%@Проверьте что если к экземпляру класса применен метод more а товаров "
            "на складе недостаточно, то в экземпляре класса не возникают лишние товары"
        )

if __name__ == "__main__":
    unittest.main()

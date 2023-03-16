import sys
import unittest
from pathlib import Path
import os
from main import Item, Cheque

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

def ordering():
    suite = unittest.TestSuite()
    suite.addTest(CheckClassesTestCase('test_classes_attrs'))
    suite.addTest(TestClassesTestCase('test_total_price'))
    return suite

class CheckClassesTestCase(SkyproTestCase):

    def test_classes_attrs(self):
        item = Item(title="test", price=500, unit="кг", quantity=100)
        self.assertTrue(
            hasattr(item, "discount_value"),
            "%@Проверьте, что в конструкторе класса Item (метод __init__) " 
            f" объявлено свойство discount_value для экземпляра"
        )
        self.assertTrue(
            hasattr(item, "_calculate_discount"),
            "%@Проверьте, что класс Item имеет внутренний метод _calculate_discount"
        )


class TestClassesTestCase(SkyproTestCase):
    
    @classmethod
    def setUpClass(self):
        self.item_with_discount = Item(
            title='Пюльмешки', 
            price=100, 
            unit='кг', 
            quantity=5, 
            discount_value = 0.2)
        self.item_without_discount = Item(
            title='Дорогие пюльмешки', 
            price=100, unit='кг', 
            quantity=5)
        self.cheque = Cheque()

    def test_total_price(self):
        self.assertTrue(
            self.item_with_discount.total_price() == 400,
            "%@Проверьте, что метод total_price работает корректно и считает скидку, если скидка"
            " передана в аргумент discount_value при создании экземпляра класса"
        )

        self.assertTrue(
            self.item_without_discount.total_price() == 500,
            "%@Проверьте, что метод total_price работает корректно если скидка у товара отсутствует"
        )
        try:
            self.cheque.add_item(title='Сушеные питоны', price=1000, unit='шт', quantity=5, discount_value=0.2)
        except TypeError:
            self.fail(
                "%@Проверьте что правильно произвели рефакторинг метода add_item класса Cheque "
                "Ошибка происходит, когды мы пытаемся передать ему аргумент discount_value со скидкой"
            )


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(ordering())


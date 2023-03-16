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

class ClassesTestCase(SkyproTestCase):
    
    @classmethod
    def setUpClass(self):
        self.item_1 = Item(title='test_1', price=1, unit='тс', quantity=3)
        self.item_2 = Item(title='test_1', price=2, unit='тс', quantity=2)
        self.cheque = Cheque()

    def test_init_returns_class_instances(self):
        item_attrs = ['title', 'price', 'unit', 'quantity']
        for attr in item_attrs:
            self.assertTrue(
                hasattr(self.item_1, attr),
                f'%@Проверьте, что экземпляр класса Item имеет аттрибут {attr}'
            )
        
        self.assertTrue(
            hasattr(self.cheque, 'items'),
            "%@Проверьте, что экземпляр класса Cheque имеет аттрибут 'items'"
        )

        self.assertIsInstance(
            self.cheque.items, list,
            "%@Проверьте, что аттрибут items класса Cheque это лист"
        )
        self.cheque.items.extend([self.item_1, self.item_2])

        self.assertTrue(
            self.cheque.purchases() == 'test_1, 3тс - 3\ntest_1, 2тс - 4',
            "%@Проверьте, в правильном ли формате возвращается список покупок "
            "при использовании функции purchases"
        )

        self.assertTrue(
            self.cheque.get_sum() == 'Сумма: 7',
            "%@Проверьте, правильно ли возвращается сумма покупок и правильно ли оформлен результат"
            " который возвращает функция get_sum "
        )


if __name__ == "__main__":
    unittest.main()

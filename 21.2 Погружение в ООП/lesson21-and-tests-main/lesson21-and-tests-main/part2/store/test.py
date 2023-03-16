import sys
import unittest
from pathlib import Path
import os
from main import Store

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

class StoreTestCase(SkyproTestCase):

    def test_init_returns_class_instances(self):

        store = Store()
        self.assertTrue(
            hasattr(store, "store"),
            "%@Проверьте что добавили в класс функцию __init__ "
            "в которой создаётся словарик store"
        )

        self.assertTrue(
            hasattr(store, '_check_item'),
            "%@Проверьте, что функция check_item была перенесена в тело класса, а её "
            "название соответсвует правилам нейминга внуренних методов класса"
        )

        try:
            store.add_item(title="пюльмени", quantity=5)
        except TypeError:
            self.fail("%@Проверьте, что убрали лишний аргумент из функции add_item")
        store.add_item(title="пюльмени", quantity=5)
        self.assertTrue(
            len(store.store) == 1,
            "%@проверьте что при применении функции add_item во внутренний словарик класса "
            "добавлятеся новая позиция, возможно вы не переименовали переменную store соответствующим "
            "образом."
        )

        try:
            store._check_item(title="пюльмени")
        except TypeError:
            self.fail(
                "%@Проверьте, что убрали лишний аргумент из функции _check_item "
                "и добавили обязательный аргумент self"
            )

        try:
            store._check_quantity_limits(title="пюльмени", quantity=5)
        except TypeError:
            self.fail(
                "%@Проверьте, что убрали лишний аргумент из функции _check_quantity_limits "
                "и не забыли переименовать переменную store в теле метода"
        )
        try:
            store.get_item(title="пюльмени", quantity=5)
        except TypeError:
            self.fail(
                "%@Проверьте, что убрали лишний аргумент из функции get_item "
                "и не забыли переименовать переменную store в теле метода"
        )
        item = store.get_item(title="пюльмени", quantity=5)
        self.assertTrue(
            item == ("пюльмени", 5),
            "%@Проверьте, что функция get_item работает корректно и возвращает товар"
        )
        self.assertTrue(
            store.store.get("пюльмени") == 0,
            "%@Проверьте, что после срабатывания функции get_item, товар на складе был списан"
        )   

if __name__ == "__main__":
    unittest.main()

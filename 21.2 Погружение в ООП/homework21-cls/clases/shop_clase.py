from abc import ABC

from clases.storage_clase import Storage
from configuración import SHOP_CAPACITY, SHOP_MAX_ITEMS


class Shop(Storage, ABC):
    """
    Класс склад
    """

    def __init__(self):
        super().__init__(SHOP_CAPACITY)
        self.shop_type = 'МАГАЗИН'

    def __repr__(self):
        return self.shop_type

    def add(self, title, amount):
        if amount <= self.get_free_space() and self.get_unique_items_count() < SHOP_MAX_ITEMS:
            self.items[title] = self.items.get(title, 0) + amount
            return True
        return False

    def remove(self, title, amount):
        if self.items.get(title, 0) >= amount:
            self.items[title] -= amount

            if self.items[title] == 0:
                del self.items[title]
            return True
        return False

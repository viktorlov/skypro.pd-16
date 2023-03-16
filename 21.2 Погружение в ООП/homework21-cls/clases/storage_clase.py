from abc import ABC, abstractmethod

from configuración import SHOP_MAX_ITEMS


class Storage(ABC):
    """
    Абстрактный класс для объектов Магазин, Склад
    """

    @abstractmethod
    def __init__(self, capacity: int = 0):
        self.items = {}
        self.capacity = capacity

    @abstractmethod
    def add(self, title, amount):
        pass

    @abstractmethod
    def remove(self, title, amount):
        pass

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

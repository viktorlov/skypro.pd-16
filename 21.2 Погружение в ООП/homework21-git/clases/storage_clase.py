from abc import ABC, abstractmethod


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

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

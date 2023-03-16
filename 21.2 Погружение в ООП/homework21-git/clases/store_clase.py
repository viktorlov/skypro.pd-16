from clases.storage_clase import Storage
from configuración import STORE_CAPACITY, STORE_ITEMS


class Store(Storage):
    """
    Класс склад
    """

    def __init__(self):
        super().__init__(STORE_CAPACITY)
        self.store_type = 'СКЛАД'
        for key, value in STORE_ITEMS.items():
            self.add(key, value)

    def __repr__(self):
        return self.store_type

    def add(self, title, amount):
        if amount <= self.get_free_space():
            self.items[title] = self.items.get(title, 0) + amount
            return True
        return False

    def remove(self, title, amount):
        if self.items.get(title, 0) >= amount:
            self.items[title] -= amount
            return True
        return False

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

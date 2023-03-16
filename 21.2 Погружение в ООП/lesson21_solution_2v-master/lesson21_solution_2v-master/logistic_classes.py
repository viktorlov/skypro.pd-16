from abc import abstractmethod, ABC


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_item(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count
                    is_found = True
            if not is_found:
                self.items[name] = count
            print("Товар добавлен")
        else:
            print(f"Товар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров")

    def remove(self, name, count):
        for key in self.items.keys():
            if name == key:
                if self.items[key] - count >= 0:
                    self.items[key] = self.items[key] - count
                else:
                    print(f"Слишком мало {name}")
            else:
                print(f"{name.title()} - нет на складе")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_item(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 30
        self._limit = limit
        self.items = {}

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_items_count() < self._limit:
            super().add(name, count)
        else:
            print(f"Товар не может быть добавлен")

    def get_unique_items_count(self):
        return len(self.items.keys())


class Request:
    def __init__(self, demand):
        lst = self.get_info(demand)

        self.from_ = lst[4]
        self.amount_ = int(lst[1])
        self.product_ = lst[2]

        if len(lst) > 6:
            self.to_ = lst[6]
        else:
            self.to_ = None

    @staticmethod
    def get_info(demand):
        return demand.split(" ")

    def __repr__(self):
        return f'Доставить** {self.amount_} {self.product_} **из** {self.from_} **в** {self.to_}'

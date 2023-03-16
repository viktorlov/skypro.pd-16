# Решение
class Store:
    def __init__(self):
        self.store = {}

    def add_item(self, title: str, quantity: int):
        self.store[title] = self.store.get(title, 0) + quantity

    def get_item(self, title, quantity):
        if not self._check_item(title=title):
            return 'Не было на складе'
        quantity = self._check_quantity_limits(title=title, quantity=quantity)
        self.store[title] -= quantity
        return title, quantity

    def _check_item(self, title: str):
        return title in self.store

    def _check_quantity_limits(self, title: str, quantity: int) -> int:
        current_qnt = self.store[title]
        if current_qnt < quantity:
            quantity = current_qnt
        return quantity


if __name__ == '__main__':
    my_store = Store()
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сырые питоны', quantity=5)
    print(my_store.get_item(title='Сушеные питоны', quantity=20))
    print(my_store.get_item(title='Сырые питоны', quantity=10))
    print(my_store.get_item(title='Сырые питоны', quantity=10))
    print(my_store.get_item(title='Админские барабаны', quantity=7))

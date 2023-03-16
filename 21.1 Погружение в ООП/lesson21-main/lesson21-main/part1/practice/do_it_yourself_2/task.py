# Исходный код

def check_item(store: dict, title: str):
    return title in store


class Store:
    def add_item(self, store: dict, title: str, quantity: int):
        store[title] = store.get(title, 0) + quantity

    def get_item(self, store: dict, title, quantity):
        if not check_item(store=store, title=title):
            return 'Не было на складе'
        quantity = self._check_quantity_limits(store=store, title=title, quantity=quantity)
        store[title] -= quantity
        return title, quantity

    def _check_quantity_limits(self, store: dict, title: str, quantity: int) -> int:
        current_qnt = store[title]
        if current_qnt < quantity:
            quantity = current_qnt
        return quantity


if __name__ == '__main__':
    # Код ниже является проверочным и должен выполняться корректно
    my_store = Store()
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сушеные питоны', quantity=10)
    my_store.add_item(title='Сырые питоны', quantity=5)
    print(my_store.get_item(title='Сушеные питоны'), quantity=20)
    print(my_store.get_item(title='Сырые питоны'), quantity=10)
    print(my_store.get_item(title='Сырые питоны'), quantity=10)
    print(my_store.get_item(title='Админские барабаны', quantity=7))

# Перейдём к мокированию метода в фикстурах.
#
# Воспользуемся сценарием из прошлой задачи(test_mock_simple)
# И предположим что у нас не один, а 3 метода, использующих
# запросы к платным сервисам. (В реальности их может быть ещё больше).
# 
# В данном случаее удобнее было бы создать экземпляр такого класса в фикстуре
# и передавать его как аргумент в тестовые функции.
#
# Попробуйте с помощью фикстуры поставить одну заглушку для всех функций.
# В качестве возвращаемого аргумента также используйте  список 
# ["Санкт-Петербург", "Самара", "Краснодар"]
#
from unittest.mock import MagicMock

import requests
import os
import pytest

# Класс, подлежащий тестированию
class AddressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_address.com?search={city}')
        return response.data

    def show_offices(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."

    def show_warehouses(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение cкладов: {cities}."

    def show_markets(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение магазинов: {cities}."

@pytest.fixture
def addressgetter():
    address_getter = AddressGetter()
    address_getter.get_cities = MagicMock(return_value=["Санкт-Петербург", "Самара", "Краснодар"])
    return address_getter

# Тесты уже готовы, Здесь ничего менять не нужно. 
# Если они сработали, значит фикстура сделана правильно
def test_show_offices(addressgetter: AddressGetter):
    expected_string = "Расположение офисов: Санкт-Петербург, Самара, Краснодар."
    assert addressgetter.show_offices() == expected_string

def test_show_warehouses(addressgetter: AddressGetter):
    expected_string = "Расположение cкладов: Санкт-Петербург, Самара, Краснодар."
    assert addressgetter.show_warehouses() == expected_string

def test_show_markets(addressgetter: AddressGetter):
    expected_string = "Расположение магазинов: Санкт-Петербург, Самара, Краснодар."
    assert addressgetter.show_markets() == expected_string

if __name__=="__main__":
    os.system("pytest")

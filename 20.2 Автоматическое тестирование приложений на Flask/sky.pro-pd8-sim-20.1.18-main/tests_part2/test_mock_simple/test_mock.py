# В этом задании Вам предстоит сделать мок метода класса.
# Представим простой сценарий:
# У нас имеется класс AddressGetter один из методов которого,
# использует услуги платных сервисов с целью получения 
# списка предлагаемых адресов (в данном случае для упрощения - городов).
# К примеру, при запросе на сторонний сервис данная функция возвращает список вида:
# ["Санкт-Петербург", "Самара", "Краснодар"].
# Каждый раз обращаться к платным сервисам для 
# тестирования было бы мягко говоря не экономично.
#
# Вместе с тем, данным методом пользуется другой метод show_cities.
# Который, преобразовывет полученный список в строку вида:
#
# Расположение офисов: Санкт-Петербург, Самара, Краснодар.
#
# Попробуйте мокнуть метод get_address класса AddressGetter, так чтобы
# show_cities работал корректно и получал необходимые ему данные.
# Для этого следуйте следующим шагам:
#
# 1. В теле тестовой функции test_show_cities:
#    - Создайте экземпляр класса AddressGetter     
#    - Cделайте мок метода get_cities класса AddressGetter
#      в качестве аргумента, используйте пожалуйста список: 
#      ["Санкт-Петербург", "Самара", "Краснодар"], это необходимо для проверки.
#    - вызовите метод в теле функции show_cities и проверьте ожидаемый результат
import pytest
from unittest.mock import MagicMock
import requests
import os

class AddressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_address.com?search={city}')
        return response.data
    
    def show_cities(self):           # Необходимо протестировать этот метод
        cities = self.get_cities()   # Здесь происходить вызов стороннего сервиса
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."

@pytest.fixture()
def addressgetter():
    address_getter = AddressGetter()
    address_getter.get_cities = MagicMock(return_value=["Санкт-Петербург", "Самара", "Краснодар"])
    return address_getter

def test_show_cities(addressgetter):
    # TODO Попробуйте мокнуть нужный метод здесь
    assert addressgetter.show_cities() == "Расположение офисов: Санкт-Петербург, Самара, Краснодар."

if __name__=="__main__":
    os.system("pytest")

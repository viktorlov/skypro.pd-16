from task import *

# Тесты


company = Company(name='ООО Классные Объекты',
                  address='г. Город, ул. Улица, д 13',
                  phone='12345678')

receipt = Receipt()
receipt.set_company(company=company)
receipt.add_item(title='Сушеные питоны', unit='упаковка.',
                 price_for_unit=100, quantity=5)
receipt.add_item(title='Книги про PHP', unit='шт.',
                 price_for_unit=1, quantity=10)
receipt.add_item(title='Кофе плохорастворенный', unit='л.',
                 price_for_unit=1000, quantity=.2)
receipt.print()

test_company = Company('', '', '')
test_item1 = Item(title='test1',
                  unit='кг',
                  price_for_unit=100,
                  quantity=0.33)
test_item2 = Item(title='test2',
                  unit='кг',
                  price_for_unit=100,
                  quantity=1)
test_item3 = Item(title='test3',
                  unit='кг',
                  price_for_unit=100,
                  quantity=1.2734)
test_receipt = Receipt()
test_receipt.set_company(company=test_company)
test_receipt.add_item(title='Сушеные питоны', unit='упаковка.',
                      price_for_unit=100, quantity=5)


def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert(hasattr(test_company, 'name'), correct='Атрибут класса Company "name" определен',
            incorrect='Атрибут класса Company "name" НЕ определен')
test_assert(hasattr(test_company, 'address'), correct='Атрибут класса Company "address" определен',
            incorrect='Атрибут класса Company "address" НЕ определен')
test_assert(hasattr(test_company, 'phone'), correct='Атрибут класса Company "phone" определен',
            incorrect='Атрибут класса Company "phone" НЕ определен')
test_assert(hasattr(test_item1, 'title'), correct='Атрибут класса Item "title" определен',
            incorrect='Атрибут класса Item "title" НЕ определен')
test_assert(hasattr(test_item1, 'unit'), correct='Атрибут класса Item "unit" определен',
            incorrect='Атрибут класса Item "unit" НЕ определен')
test_assert(hasattr(test_item1, 'price_for_unit'), correct='Атрибут класса Item "price_for_unit" определен',
            incorrect='Атрибут класса Item "price_for_unit" НЕ определен')
test_assert(hasattr(test_item1, 'quantity'), correct='Атрибут класса Item "quantity" определен',
            incorrect='Атрибут класса Item "quantity" НЕ определен')
test_assert(test_receipt.company == test_company, correct='Функция "set_company" класса Receipt реализована верно',
            incorrect='Функция "set_company" класса Receipt реализована НЕ верно')
test_assert(isinstance(test_receipt.items[0], Item), correct='Функция "add_item" класса Receipt реализована верно',
            incorrect='Функция "add_item" класса Receipt реализована НЕ верно')
test_assert(all((isinstance(test_item1.get_price(), float),
                 isinstance(test_item2.get_price(), float),
                 isinstance(test_item3.get_price(), float))),
            correct='Метод get_price класса Item корректно возвращает "float"',
            incorrect='Метод get_price класса Item должен возвращать "float"')

test_assert(all((test_item1.get_price() == 33.0,
                 test_item2.get_price() == 100.0,
                 test_item3.get_price() == 127.34)),
            correct='Метод get_price класса Item корректно считает цены',
            incorrect='Метод get_price класса Item не корректно считает цены')

test_assert(globals().get('company', False), correct='Объект "company" создан',
            incorrect='Объект "company" нельзя удалять')
test_assert(globals().get('receipt', False), correct='Объект "receipt" создан',
            incorrect='Объект "receipt" нельзя удалять')

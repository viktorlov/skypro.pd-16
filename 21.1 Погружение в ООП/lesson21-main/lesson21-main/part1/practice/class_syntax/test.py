from task import *
import sys

company = Company(name='ООО Классные Объекты',
                  address='г. Город, ул. Улица, д 13',
                  phone='12345678')

dry_pythons = Item(title='Сушеные питоны, упаковка', price=500)
php_books = Item(title='Книги про PHP, шт', price=10)
questionable_coffe = Item(title='Кофе плохорастворенный, шт', price=200)

receipt = Receipt()
receipt.company = company
receipt.items.extend([dry_pythons, php_books, questionable_coffe])
receipt.print()

# Teсты

test_company = Company('', '', '')
test_item = Item('', 1)


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
test_assert(hasattr(test_item, 'title'), correct='Атрибут класса Item "title" определен',
            incorrect='Атрибут класса Item "title" НЕ определен')
test_assert(hasattr(test_item, 'price'), correct='Атрибут класса Item "price" определен',
            incorrect='Атрибут класса Item "price" НЕ определен')
test_assert(globals().get('company', False), correct='Объект "company" создан',
            incorrect='Объект "company" нельзя удалять')
test_assert(globals().get('dry_pythons', False), correct='Объект "dry_pythons" создан',
            incorrect='Объект "dry_pythons" нельзя удалять')
test_assert(globals().get('php_books', False), correct='Объект "php_books" создан',
            incorrect='Объект "php_books" нельзя удалять')
test_assert(globals().get('questionable_coffe', False), correct='Объект "questionable_coffe" создан',
            incorrect='Объект "questionable_coffe" нельзя удалять')
test_assert(globals().get('receipt', False), correct='Объект "receipt" создан',
            incorrect='Объект "receipt" нельзя удалять')
company = Company(name='ООО Классные Объекты',
                  address='г. Город, ул. Улица, д 13',
                  phone='12345678')

dry_pythons = Item(title='Сушеные питоны, упаковка', price=500)
php_books = Item(title='Книги про PHP, шт', price=10)
questionable_coffe = Item(title='Кофе плохорастворенный, шт', price=200)

receipt = Receipt()
receipt.company = company
receipt.items.extend([dry_pythons, php_books, questionable_coffe])
receipt.print()

# Teсты

test_company = Company('', '', '')
test_item = Item('', 1)


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
test_assert(hasattr(test_item, 'title'), correct='Атрибут класса Item "title" определен',
            incorrect='Атрибут класса Item "title" НЕ определен')
test_assert(hasattr(test_item, 'price'), correct='Атрибут класса Item "price" определен',
            incorrect='Атрибут класса Item "price" НЕ определен')
test_assert(globals().get('company', False), correct='Объект "company" создан',
            incorrect='Объект "company" нельзя удалять')
test_assert(globals().get('dry_pythons', False), correct='Объект "dry_pythons" создан',
            incorrect='Объект "dry_pythons" нельзя удалять')
test_assert(globals().get('php_books', False), correct='Объект "php_books" создан',
            incorrect='Объект "php_books" нельзя удалять')
test_assert(globals().get('questionable_coffe', False), correct='Объект "questionable_coffe" создан',
            incorrect='Объект "questionable_coffe" нельзя удалять')
test_assert(globals().get('receipt', False), correct='Объект "receipt" создан',
            incorrect='Объект "receipt" нельзя удалять')

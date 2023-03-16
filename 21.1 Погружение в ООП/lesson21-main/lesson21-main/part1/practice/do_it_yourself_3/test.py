from test import *


# Тесты
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert('Server' in globals(), correct='Выделен общий класс Server',
            incorrect='Нужно определить класс-родитель Server')
test_assert('add_ports' in Server.__dict__, correct='У класса Server есть метод "add_ports"',
            incorrect='У класса Server отсутствует метод "add_ports"')
test_assert('add_visible_server' in Server.__dict__, correct='У класса Server есть метод "add_visible_server"',
            incorrect='У класса Server отсутствует метод "add_visible_server"')
test_assert('get_title' in Server.__dict__, correct='У класса Server есть метод "get_title"',
            incorrect='У класса Server отсутствует метод "get_title"')
test_assert('get_opened_ports' in Server.__dict__, correct='У класса Server есть метод "get_opened_ports"',
            incorrect='У класса Server отсутствует метод "get_opened_ports"')
test_assert('get_visitable_severs' in Server.__dict__, correct='У класса Server есть метод "get_visitable_severs"',
            incorrect='У класса Server отсутствует метод "get_visitable_severs"')
test_assert('check_connection' in Server.__dict__, correct='У класса Server есть метод "check_connection"',
            incorrect='У класса Server отсутствует метод "check_connection"')
test_assert('_check_visibility' in Server.__dict__, correct='У класса Server есть метод "_check_visibility"',
            incorrect='У класса Server отсутствует метод "_check_visibility"')
test_assert('_check_is_visible_server' in Server.__dict__,
            correct='У класса Server есть метод "_check_is_visible_server"',
            incorrect='У класса Server отсутствует метод "_check_is_visible_server"')
test_assert('_check_opened_ports' in Server.__dict__, correct='У класса Server есть метод "_check_opened_ports"',
            incorrect='У класса Server отсутствует метод "_check_opened_ports"')

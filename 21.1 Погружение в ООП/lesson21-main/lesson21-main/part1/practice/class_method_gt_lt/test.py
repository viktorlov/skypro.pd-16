# Тесты

# todo тесты не работают
def test_assert(condition, correct, incorrect):
    try:
        assert condition, incorrect
        print(correct)
    except AssertionError as e:
        print(e.args[0])


test_assert(
    output_data == ['Создан объект Python. Количество 4. Осталось 6',
                    'Теперь у объекта Python 8 единиц. На складе 2',
                    'Теперь у объекта Python 5 единиц. На складе 5',
                    'Теперь у объекта Python 10 единиц. На складе 0',
                    'False'], correct='Вывод в консоль верный', incorrect='Вывод в консоль НЕ верный')

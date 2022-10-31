def get_grade(grade):
    if type(grade) == int and (2 <= grade <= 5):
        v2, v3, v4, v5 = grade == 2, grade == 3, grade == 4, grade == 5
        return v2 * "Плохо" + v3 * "Удовлетворительно" + v4 * "Хорошо" + v5 * "Отлично"
    else:
        return "Ошибка"


if __name__ == '__main__':
    print(get_grade(""))
    print(get_grade(5))
    print(get_grade(4))
    print(get_grade(3))
    print(get_grade(2))

# try:
#     assert get_grade("") == "Ошибка"
#     assert get_grade(5) == "Отлично"
#     assert get_grade(4) == "Хорошо"
#     assert get_grade(3) == "Удовлетворительно"
#     assert get_grade(2) == "Плохо"
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")

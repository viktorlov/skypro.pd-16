grades = {2: "Плохо",
          3: "Удовлетворительно",
          4: "Хорошо",
          5: "Отлично",
          }


def get_grade(grade):
    return grades.get(grade, "Ошибка")


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

GRADES = {2: "Плохо", 3: "Норм", 4: "Хорошо", 5: "Отлично"}


def get_grade(arg: int):
    try:
        return GRADES[arg]
    except KeyError:
        return f'not a grade'


if __name__ == '__main__':
    print(get_grade(-1))
    print(get_grade(1))
    print(get_grade(2))
    print(get_grade(3))
    print(get_grade(4))
    print(get_grade(5))
    print(get_grade(6))
    print(get_grade("5"))

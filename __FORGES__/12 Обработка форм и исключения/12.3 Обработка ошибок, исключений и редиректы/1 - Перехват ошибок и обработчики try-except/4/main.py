WEEKDAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]


def day_of_the_week(arg: int) -> str:
    try:
        if arg not in [1, 2, 3, 4, 5, 6, 7, ]:
            raise ValueError
        return WEEKDAYS[arg - 1]
    except (IndexError, TypeError, ValueError):
        return f'__ERROR__: no such day of the week'


if __name__ == '__main__':
    print(day_of_the_week(-1))
    print(day_of_the_week(0))
    print(day_of_the_week(1))
    print(day_of_the_week(2))
    print(day_of_the_week(3))
    print(day_of_the_week(4))
    print(day_of_the_week(5))
    print(day_of_the_week(6))
    print(day_of_the_week(7))
    print(day_of_the_week(8))
    print(day_of_the_week("8"))

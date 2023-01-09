def get_max_of_two(arg1: float, arg2: float) -> float | str:
    try:
        if not type(arg1) == type(arg2) == float:
            raise TypeError
        return max(arg1, arg2)
    except TypeError:
        return f'__TYPE-ERROR__: invalid argument'


if __name__ == '__main__':
    print(get_max_of_two(1.0, 2.0))
    print(get_max_of_two(1.0, 3.0))
    print(get_max_of_two(1.0, 5.0))
    print(get_max_of_two(1.0, 10.0))
    print(get_max_of_two(1, 2.0))
    print(get_max_of_two(1.0, 2))
    print(get_max_of_two(1, 2))
    print(get_max_of_two(1.0, "2"))
    print(get_max_of_two("1", 2.0))
    print(get_max_of_two("1", "!"))
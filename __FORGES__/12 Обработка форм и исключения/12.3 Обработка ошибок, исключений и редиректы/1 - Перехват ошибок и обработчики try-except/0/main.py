def divider(a: [int | float], b: [int | float]):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = 0.0
    return result


if __name__ == '__main__':
    print(divider(1, 1))
    print(divider(1, 0))
    print(divider(0, 1))
    print(divider(0, 0))
    print(divider("0", 0))
    print(divider(0, "0"))
    print(divider("0", "0"))

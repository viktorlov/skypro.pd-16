from num2words import num2words

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]


def digit_to_word(arg: int) -> str:
    try:
        if arg not in DIGITS:
            raise ValueError
        return num2words(arg)
    except ValueError:
        return '__VALUE-ERROR__: not a valid digit'


if __name__ == '__main__':
    print(digit_to_word(-1))
    print(digit_to_word(0))
    print(digit_to_word(1))
    print(digit_to_word(3))
    print(digit_to_word(5))
    print(digit_to_word(7))
    print(digit_to_word(7.0000))
    print(digit_to_word(7.00001))
    print(digit_to_word("7"))

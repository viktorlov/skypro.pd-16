def validate_pin(pin):
    """ Проверяет, является ли ПИН-код последовательностью 4 цифр """

    if not pin.isdigit():
        return False
    if len(pin) != 4:
        return False
    return True


if __name__ == '__main__':
    print(validate_pin("1111"))

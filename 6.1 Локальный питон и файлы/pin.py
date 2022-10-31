def check_pin(pin):
    return True if len(pin) == 4 * pin.isdigit() else False


if __name__ == '__main__':
    print(check_pin("1234"))
    print(check_pin("123"))
    print(check_pin("a000"))
    print(check_pin("0000"))

# try:
#     assert check_pin("1234") == True
#     assert check_pin("123") == False
#     assert check_pin("a000") == False
#     assert check_pin("0000") == True
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
# else:
#     print("Все хорошо, все работает")

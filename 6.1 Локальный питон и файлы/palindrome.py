def is_palindrome(word):
    return True if word == word[::-1] else False


if __name__ == '__main__':
    print(is_palindrome("level"))
    print(is_palindrome("sagas"))
    print(is_palindrome("hero"))
    print(is_palindrome("drama"))

# try:
#     assert is_palindrome("level") == True
#     assert is_palindrome("sagas") == True
#     assert is_palindrome("hero") == False
#     assert is_palindrome("drama") == False
#
# except AssertionError:
#     print("Неверно, проверьте функцию на разных значениях")
#
# else:
#     print("Все хорошо, все работает")

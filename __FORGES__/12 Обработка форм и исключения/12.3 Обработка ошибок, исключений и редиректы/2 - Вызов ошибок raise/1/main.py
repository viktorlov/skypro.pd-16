def digits_count(arg: int) -> str:
    try:
        if type(arg) is not int:
            raise TypeError
        return len(str(abs(arg)))
    except TypeError:
        return '__TYPE-ERROR__: not an integer'

if __name__ == '__main__':
    print(digits_count(-1))
    print(digits_count(-20))
    print(digits_count(-300))
    print(digits_count(-4000))
    print(digits_count(0))
    print(digits_count(10))
    print(digits_count(300))
    print(digits_count(5000))
    print(digits_count(70000))
    print(digits_count(7.0000))
    print(digits_count(7.00001))
    print(digits_count("7"))
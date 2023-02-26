# Напишите декоратор called, 
# который при вызове функции будет перед 
# вызовом функции выводить в консоль "функция вызвана"
def called(function):
    def wrapper():
        print("something")
        return function()

    return wrapper


# Ниже следует код для самопроверки:
# TODO Вы можете попробовать задекорировать функцию func
# в теле которой ничего не происходит.

@called
def func():
    pass


if __name__ == "__main__":
    func()

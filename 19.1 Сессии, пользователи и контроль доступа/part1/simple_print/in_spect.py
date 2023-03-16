

def called(function):
    def wrapper():
        from pathlib import Path
        print(f'\n\t{Path(__file__) = }\n\t{function.__name__ = }\n')
        return function()
    return wrapper

@called
def func():
    print("bla-bla-bla-bla-bla-bla-bla")
    pass


if __name__ == "__main__":
    func()

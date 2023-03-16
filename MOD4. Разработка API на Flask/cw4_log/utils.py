# Licensed under the Apache License, Version 2.0 (the "License");
# ----------------------------------------------------------------
# ok
# ----------------------------------------------------------------
import functools
import json
from typing import Union


def called(function):
    def wrapper(*args, **kwargs):
        pass
        return function(*args, **kwargs)

    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"\n\t\t\tВызываем {func.__name__}({signature})\n")
        value = func(*args, **kwargs)
        print(f"\n\t\t\t{func.__name__!r} возвращает {value!r}\n")  # 4
        return value

    return wrapper_debug


@debug
def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)

# from app1_ import print_args
from app2_ import print_args


def test_print_args():
    # Test with only positional arguments
    assert print_args(1, 2, 3) == [1, 2, 3]

    # Test with only keyword arguments
    assert print_args(a=4, b=5, c=6) == [{'a': 4}, {'b': 5}, {'c': 6}]

    # Test with both positional and keyword arguments
    assert print_args('x', 'y', z=7) == ['x', 'y', {'z': 7}]

    # Test with no arguments
    assert print_args() == []

    # Test with empty keyword arguments
    assert print_args(1, 2, {}) == [1, 2, {}]

    # Test with iterable positional argument
    assert print_args(*"name") == ['n', 'a', 'm', 'e']

    # Test with iterable keyword argument
    assert print_args(a=[1, 2, 3]) == [{'a': [1, 2, 3]}]

    # Test with a combination of iterable and non-iterable arguments
    assert print_args(*"name", a="surname", b=['first', 'second']) == ['n', 'a', 'm', 'e', {'a': 'surname'},
                                                                       {'b': ['first', 'second']}]

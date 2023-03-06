import pytest


def test_ok(number_42):
    assert number_42 == 42


@pytest.mark.xfail()
def test_failed(number_42):
    test = "'"
    a = f"{test}"
    print(a)
    assert number_42 == 2

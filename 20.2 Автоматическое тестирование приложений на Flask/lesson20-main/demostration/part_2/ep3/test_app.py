from unittest.mock import MagicMock

import pytest

from app import ProductionClass


@pytest.fixture()
def prod_class():
    pc = ProductionClass()
    pc.m1 = MagicMock(return_value="123")
    pc.m2 = MagicMock(return_value="321")
    return pc


def test_pc(prod_class):
    assert prod_class.m1() == "123"
    assert prod_class.m2() == "321"

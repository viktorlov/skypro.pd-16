import pytest

from utils import get_period

period_parameters = [(0, 'ночь'),
                     (1, 'ночь'),
                     (6, 'ночь'),
                     (7, 'утро'),
                     (8, 'утро'),
                     (11, 'утро'),
                     (12, 'день'),
                     (13, 'день'),
                     (17, 'день'),
                     (18, 'вечер'),
                     (19, 'вечер'),
                     (24, 'вечер'), ]


@pytest.mark.parametrize("period_int, period_str", period_parameters)
def test_get_period(period_int, period_str):
    assert get_period(period_int) == period_str


period_exceptions = [(-1, ValueError),
                    (25, ValueError),
                    ("5", TypeError),
                    (5.0, TypeError), ]


@pytest.mark.parametrize("period_int, exception", period_exceptions)
def test_get_period_exceptions(period_int, exception):
    with pytest.raises(exception):
        get_period(period_int)

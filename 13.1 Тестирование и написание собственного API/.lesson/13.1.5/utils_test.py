import pytest

from utils import ticket_price

age_2_cost = [(0, 'Бесплатно'),
        (1, 'Бесплатно'),
        (7, '100 рублей'),
        (18, '200 рублей'),
        (25, '300 рублей'),
        (60, 'Бесплатно'),
        (0.5, 'Бесплатно'),
        (-1, 'Ошибка'), ]


@pytest.mark.parametrize('age, cost', age_2_cost)
def test_ticket_price(age, cost):
    assert ticket_price(age) == cost

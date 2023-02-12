def get_grade(points):
    if points < 41:
        return "Плохо"
    if points < 61:
        return "Удовлетворительно"
    if points < 81:
        return "Хорошо"
    return "Отлично"


import pytest

parametries = [(0, 'Плохо'),
               (40, 'Плохо'),
               (41, 'Удовлетворительно'),
               (42, 'Удовлетворительно'),
               (61, 'Хорошо'),
               (62, 'Хорошо'),
               (0.5, 'Плохо'),
               (-1, 'Плохо'), ]


@pytest.mark.parametrize('key_, value_', parametries)
def test_get_grade(key_, value_):
    assert get_grade(key_) == value_, 'Error found!'

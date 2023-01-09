import pytest

from utils import get_grade

grade_parameters = [(0, 2),
                    (1, 2),
                    (19, 2),
                    (20, 3),
                    (21, 3),
                    (39, 3),
                    (40, 4),
                    (41, 4),
                    (79, 4),
                    (80, 5),
                    (81, 5),
                    (100, 5), ]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_get_grade(grade_int, grade_str):
    assert get_grade(grade_int) == grade_str


grade_exceptions = [(-1, ValueError),
                    (101, ValueError),
                    ("5", TypeError),
                    (5.0, TypeError), ]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_get_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_grade(grade_int)

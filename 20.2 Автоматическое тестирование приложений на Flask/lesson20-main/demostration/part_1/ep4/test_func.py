import pytest

from app import sum_func, call_method


class TestSumFunc:
    def test_sum_positive(self):
        c = sum_func(1, 1)
        assert c > 0
        assert c == 2

    def test_sum_positive_and_negative(self):
        c = sum_func(1, -1)
        assert c == 0

    def test_sum_negative2(self):
        c = sum_func(-30, -10)
        assert c < 0
        assert c == -40

    triplets = [(1, 2, 3), (3, 4, 7), (-3, -4, -7)]

    triplets_ids = ['Triplet({}+{}={})'.format(p[0], p[1], p[2]) for p in triplets]

    @pytest.mark.parametrize('tripl', triplets, ids=triplets_ids)
    def test_sum_numbers(self, tripl):
        assert (tripl[0] + tripl[1]) == tripl[2]

    def test_has_to_fail(self):
        with pytest.raises(Exception):
            call_method()

    @pytest.mark.skip(reason="OK")
    def test_skip(self):
        raise Exception()

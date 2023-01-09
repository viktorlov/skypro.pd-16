import pytest

from player import Player


class TestPlayer:

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            Player('A')

    def test_change_name_value_error(self):
        player = Player('AAA')
        with pytest.raises(ValueError):
            player.change_name('B')

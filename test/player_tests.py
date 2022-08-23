import pytest

from src.player import Player


def test_unique_stats_list():
    # makes sure each player stats list is unique to that player
    harper = Player("Harper", 34, "RF")
    assert harper.get_stat("H") == 0
    harper.add_stat("H", 1)
    assert harper.get_stat("H") == 1

    utley = Player("Utley", 26, "2B")
    assert utley.get_stat("H") == 0


def test_players_equal_each_other():
    howard = Player("Howard", 6, "1B")
    howard_copy = Player("Howard", 6, "1B")
    harper = Player("Harper", 34, "RF")

    assert howard.__eq__(howard_copy)
    assert not harper.__eq__(howard)
    assert harper.__eq__(harper)


@pytest.mark.parametrize("player, expected", [
    (Player("Bryce Harper", 34, "RF"), "Bryce Harper"),
    (Player("Ryan Howard", 6, "1B"), "Ryan Howard"),
    (Player("Chase Utley", 26, "2B"), "Chase Utley")
])
def test_get_name(player, expected):
    assert player.get_name() == expected


@pytest.mark.parametrize("player, expected", [
    (Player("Bryce Harper", 34, "RF"), 34),
    (Player("Ryan Howard", 6, "1B"), 6),
    (Player("Chase Utley", 26, "2B"), 26)
])
def test_get_number(player, expected):
    assert player.get_number() == expected


@pytest.mark.parametrize("player, expected", [
    (Player("Bryce Harper", 34, "RF"), "RF"),
    (Player("Ryan Howard", 6, "1B"), "1B"),
    (Player("Chase Utley", 26, "2B"), "2B")
])
def test_get_number(player, expected):
    assert player.get_position() == expected


def test_invalid_position():
    with pytest.raises(ValueError):
        Player("Bryce Harper", 34, "dog tired")

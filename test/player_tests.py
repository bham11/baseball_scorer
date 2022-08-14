from src.player import Player


def test_stats():
    harper = Player("Harper", 34, "RF")
    assert harper.get_stat("H") == 0
    harper.add_stat("H", 1)
    assert harper.get_stat("H") == 1
from src.player import Player


def test_unique_stats_list():
    # makes sure each player stats list is unique to that player
    harper = Player("Harper", 34, "RF")
    assert harper.get_stat("H") == 0
    harper.add_stat("H", 1)
    assert harper.get_stat("H") == 1

    utley = Player("Utley", 26, "2B")
    assert utley.get_stat("H") == 0

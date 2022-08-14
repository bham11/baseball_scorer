from src.res.stats_template import PITCHER, BATTER


class Player:
    def __init__(self, name: str, number: int, position):
        self._name = name
        self._number = number
        self._position = position
        if self._position == "pitcher":
            base_stats = PITCHER
        else:
            base_stats = BATTER
        self.stats = base_stats

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_position(self):
        return self._position

    def get_stat(self, key):
        return self.stats.get(key, None)

    def add_stat(self, key, amt):
        self.stats[key] += amt


def test_stats():
    harper = Player("Harper", 34, "RF")
    assert harper.get_stat("H") == 0
    harper.add_stat("H", 1)
    assert harper.get_stat("H") == 1


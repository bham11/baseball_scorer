from src.res.stats_template import PITCHER, BATTER


class Player:
    """
    represents a baseball player
    """

    def __init__(self, name: str, number: int, position):
        """

        :param name: name of the player
        :param number: number the player wears
        :param position: what position the player plays
        """
        self._name = name
        self._number = number
        self._position = position
        if self._position == "pitcher":
            base_stats = PITCHER.copy()
        else:
            base_stats = BATTER.copy()
        self.stats = base_stats

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_position(self):
        return self._position

    def get_stat(self, key):
        """

        :param key: the stat to look up
        :return: the value of that statistic
        """
        return self.stats.get(key, None)

    def add_stat(self, key, amt):
        """

        :param key: the stat to add to
        :param amt: the amount to add
        :return: (void) updates the internal stats table
        """
        self.stats[key] += amt

    def __eq__(self, other):
        return isinstance(other, Player) and other._name == self._name and other._number == self._number

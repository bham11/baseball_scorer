from inning import Inning
from player import Player


class AtBat:
    def __init__(self, batter: Player, pitcher: Player, inn: Inning):
        """

        :param batter: the batter in the at-bat
        :param pitcher: the pitcher of the at-bat
        :param inn: what inning this at-bat takes place in
        """
        self._batter = batter
        self._pitcher = pitcher
        self._inning = inn
        self._balls = 0
        self._strikes = 0
        self._result = None

    def throw_ball(self):
        """

        :return: either the batter walks, or we add another ball to the count
        """
        if self._balls + 1 == 4:
            self._balls = 0
            self._result = "BB"
            self._pitcher.add_stat("BB", 1)
            self._batter.add_stat("BB", 1)
            self._inning.add_to_log(self)
        elif self._balls + 1 < 4:
            self._balls += 1

    def throw_strike(self):
        """

        :return: either the batter strikes out or we add another strike to the count
        """
        if self._strikes + 1 == 3:
            self._strikes = 0
            self._result = "K"
            self._inning.make_out(self)
            self._pitcher.add_stat("K", 1)
            self._batter.add_stat("K", 1)
            self._inning.add_to_log(self)
        else:
            self._strikes += 1

    def get_batter(self):
        return self._batter

    def get_pitcher(self):
        return self._pitcher

    def get_result(self):
        return self._result

    def ball_in_play(self, action: str):
        pass

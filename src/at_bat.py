from inning import Inning
from player import Player


class AtBat:
    def __init__(self, batter: Player, pitcher: Player, inn: Inning):
        self._batter = batter
        self._pitcher = pitcher
        self._inning = inn
        self._balls = 0
        self._strikes = 0
        self.result = None

    def throw_ball(self):
        if self._balls + 1 == 4:
            self._balls = 0
            self.result = "BB"
            self._pitcher.add_stat("BB", 1)
            self._batter.add_stat("BB", 1)
            # add to inning log
        elif self._balls + 1 < 4:
            self._balls += 1

    def throw_strike(self):
        # an inning should have at-bats or should an at_bat have an inning?
        if self._strikes + 1 == 3:
            self._strikes = 0
            self.result = "K"
            self._inning.make_out(self)
            self._pitcher.add_stat("K", 1)
            self._batter.add_stat("K", 1)
            # add to inning log
        else:
            self._strikes += 1

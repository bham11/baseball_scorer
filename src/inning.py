from at_bat import AtBat
from team import Team


class Inning:
    def __init__(self, number, batting: Team, fielding: Team):
        self._inning_number = number
        self._cur_batting = batting
        # or make these two half innings, and they keep track of the outs
        self._cur_pitching = fielding
        self._inning_over = False
        self._logs = []
        self._outs = []

    def make_out(self, ab: AtBat):
        if len(self._outs) == 2:
            self._outs.append(ab.result)
            # switch who's batting and who's pitching, it's the end of the top of the inning
            self._cur_batting = self._cur_pitching
            self._cur_pitching = self._cur_batting
            self._logs.append()
        elif len(self._outs) == 5:
            self._outs.append(ab.result)
            self._inning_over = True







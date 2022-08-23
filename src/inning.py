from at_bat import AtBat
from res.stats_template import OUTS
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
            self._outs.append(ab.get_result())
            # switch who's batting and who's pitching, it's the end of the top of the inning
            self._cur_batting = self._cur_pitching
            self._cur_pitching = self._cur_batting
            self.add_out_to_log(ab)
        elif len(self._outs) == 5:
            self._outs.append(ab.get_result())
            self.add_out_to_log(ab)
            self._logs.append(f"Inning number {self._inning_number} is over")
            self._inning_over = True

    def add_out_to_log(self, at_bat: AtBat):
        if at_bat.get_result() in OUTS:
            if at_bat.get_result() == "K":
                this_out = f"{at_bat.get_pitcher()} struck out {at_bat.get_batter()}"
            else:
                this_out = f"{at_bat.get_batter()} recorded an out: {at_bat.get_result()}"
            self._logs.append(this_out)
        else:
            self._logs.append(f"{at_bat.get_batter()} hit a {at_bat.get_result()}")

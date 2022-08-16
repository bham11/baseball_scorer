from inning import Inning
from res.stats_template import SCOREBOARD
from team import Team


class Game:
    def __init__(self, home: Team, away: Team):
        self._home = home
        self._away = away
        self._score = SCOREBOARD
        self._innings = [Inning(x) for x in range(1, 9)]

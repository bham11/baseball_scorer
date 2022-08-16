from player import Player


class Team:
    def __init__(self, name: str, location: str, lineup: [] = None):
        self._name = name
        self._location = location
        self._lineup = lineup

    def get_team_name(self):
        return self._name

    def get_team_location(self):
        return self._location

    def get_lineup(self):
        return self._lineup

    def add_player_to_lineup(self, loc: int, player: Player):
        if loc <= 9:
            self._lineup[loc] = player
        else:
            pass

    def make_sub(self, player_to_sub: Player, player_coming_out: Player):
        batting_spot = self._lineup.index(player_coming_out)
        if player_coming_out.get_position() == player_to_sub.get_position():
            self._lineup[batting_spot] = player_to_sub

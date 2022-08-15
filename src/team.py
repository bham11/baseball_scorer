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

    def make_sub(self, player_to_sub:Player, player_coming_out:Player):
        if player_coming_out.get_position() == player_to_sub.get_position():
            self._lineup = [player_to_sub if item == player_coming_out
                            else item for item in self._lineup]

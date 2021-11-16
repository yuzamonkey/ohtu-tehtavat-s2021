from player import Player


class PlayerStats:
    def __init__(self, player_reader):
        self._players = self._read_players_from_res(
            player_reader.get_response())

    def _read_players_from_res(self, res):
        players = []
        for player_dict in res:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
            )
            players.append(player)
        return players

    def top_scorers_by_nationality(self, nationality):
        filtered = filter(lambda p: p.nationality ==
                          nationality, self._players)
        return sorted(filtered, key=Player.p_sort, reverse=True)

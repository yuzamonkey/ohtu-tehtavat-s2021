import requests
from player import Player


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
            )

            players.append(player)

    players = sorted(players, key=Player.p_sort, reverse=True)
    for player in players:
        print(player)


if __name__ == "__main__":
    main()

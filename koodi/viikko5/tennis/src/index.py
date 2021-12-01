from tennis_game import TennisGame


def main():
    game = TennisGame("Marko", "Janne")

    print(game.get_score())

    game.won_point("Marko")
    print(game.get_score())

    game.won_point("Marko")
    print(game.get_score())

    game.won_point("Janne")
    print(game.get_score())

    game.won_point("Marko")
    print(game.get_score())

    game.won_point("Marko")
    print(game.get_score())


if __name__ == "__main__":
    main()

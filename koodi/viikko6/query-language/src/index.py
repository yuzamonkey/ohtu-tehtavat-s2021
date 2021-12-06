from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    #matcher = All()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()

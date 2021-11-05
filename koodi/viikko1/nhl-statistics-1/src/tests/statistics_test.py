import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
      self.statistics = Statistics(PlayerReaderStub())

    def test_return_player_by_name(self):
        name = "Semenko"
        result = self.statistics.search(name)
        self.assertAlmostEqual(result.name, name)
    
    def test_false_name_returns_none(self):
        name = "Foobar"
        result = self.statistics.search(name)
        self.assertAlmostEqual(result, None)
      
    def test_return_team(self):
        result = self.statistics.team("EDM")
        self.assertAlmostEqual(result[0].name, "Semenko")
        self.assertAlmostEqual(result[1].name, "Kurri")
        self.assertAlmostEqual(result[2].name, "Gretzky")

    def test_top_scorers(self):
        result = self.statistics.top_scorers(3)
        self.assertAlmostEqual(result[0].name, "Gretzky")
        self.assertAlmostEqual(result[1].name, "Lemieux")
        self.assertAlmostEqual(result[2].name, "Yzerman")
        
import unittest
from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player


class UnitTests(unittest.TestCase):

    def test_player_vs_quincy(self):
        actual = play(player, quincy, 1000)
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.')

    def test_player_vs_abbey(self):
        actual = play(player, abbey, 1000)
        self.assertTrue(
            actual,
            'Expected player to defeat abbey at least 60% of the time.')

    def test_player_vs_kris(self):
        actual = play(player, kris, 1000)
        self.assertTrue(
            actual,
            'Expected player to defeat kris at least 60% of the time.')

    def test_player_vs_mrugesh(self):
        actual = play(player, mrugesh, 1000)
        self.assertTrue(
            actual,
            'Expected player to defeat mrugesh at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
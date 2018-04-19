from unittest import TestCase
from GuessingGame.guessingGame import GuessingGame


class TestGuessingGame(TestCase):

    def test_check_if_given_number_correct(self):
        connection = 0
        test_game = GuessingGame(connection)
        self.assertEqual(test_game.check_if_given_number_correct(55), True)
        self.assertEqual(test_game.check_if_given_number_correct(0), True)
        self.assertEqual(test_game.check_if_given_number_correct(99), True)
        self.assertEqual(test_game.check_if_given_number_correct(-1), False)
        self.assertEqual(test_game.check_if_given_number_correct(100), False)

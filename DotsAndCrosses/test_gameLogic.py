from unittest import TestCase
from DotsAndCrosses.gamelogic import GameLogic


class TestGameLogic(TestCase):

    def test_check_if_given_field_correct(self):
        connection = 0
        game = GameLogic(connection)
        self.assertEqual(game.check_if_given_field_correct(4), True)
        self.assertEqual(game.check_if_given_field_correct(9), False)
        self.assertEqual(game.check_if_given_field_correct(-1), False)

    def test_winning_condition_increment(self):
        connection = 0
        test_game = GameLogic(connection)
        test_game.winning_condition_increment(0, 1)
        test_rows = [1, 0, 0]
        test_columns = [1, 0, 0]
        test_diagonals = [1, 0]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")
        test_game.winning_condition_increment(6, 1)
        test_rows = [1, 0, 1]
        test_columns = [2, 0, 0]
        test_diagonals = [1, 1]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")
        test_game.winning_condition_increment(5, -1)
        test_rows = [1, -1, 1]
        test_columns = [2, 0, -1]
        test_diagonals = [1, 1]
        self.assertEqual(test_rows, test_game.rows, "Rows condition is wrong")
        self.assertEqual(test_columns, test_game.columns, "Column condition is wrong")
        self.assertEqual(test_diagonals, test_game.diagonals, "Diagonal conditions are wrong")

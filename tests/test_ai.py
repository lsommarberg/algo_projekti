import unittest
from tic_tac_toe import TicTacToe
from ai import max_value


class TestGame(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()

    def test_minimax(self):
        board = [["o", " ", "x"], ["x", "o", " "], [" ", " ", "x"]]

        moves = [(0, 1), (1, 2), (2, 0), (2, 1)]
        last_move = (2, 2)
        expected_move = (1, 2)

        _, actual_move = max_value(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
        )

        self.assertEqual(actual_move, expected_move)

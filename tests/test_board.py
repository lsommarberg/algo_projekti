import unittest
from unittest.mock import patch
from io import StringIO
from board import Board


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_board = [[" " for _ in range(20)] for _ in range(20)]
        self.mock_board[0][0] = "x"
        self.mock_small_board = [["x", " ", " "], [" ", "o", " "], [" ", " ", " "]]
        self.board_3x3 = Board(size=3)
        self.board_4x4 = Board(size=4)
        self.tictactoe = Board()

    def test_initialization(self):
        self.assertEqual(self.tictactoe.current_player, "x")

    def test_valid_move(self):
        self.tictactoe.board = self.mock_board
        row, col = 2, 1
        is_valid = self.tictactoe.is_valid_move(row, col)
        self.assertTrue(is_valid)

    def test_not_valid_move(self):
        self.tictactoe.board = self.mock_board
        row, col = 0, 0
        is_valid = self.tictactoe.is_valid_move(row, col)
        self.assertFalse(is_valid)

    def test_print_board_3x3(self):
        expected_output = (
            "  1 2 3"
            "\n --------\n"
            "1 | | | |\n"
            " --------\n"
            "2 | | | |\n"
            " --------\n"
            "3 | | | |\n"
            " --------\n"
        )

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.board_3x3.print_board()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()

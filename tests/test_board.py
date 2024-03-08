import unittest
from unittest.mock import patch
from io import StringIO
from board import Board


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_board = [[" " for _ in range(20)] for _ in range(20)]
        self.mock_board[0][0] = "x"
        self.mock_small_board = [["x", " ", " "], [" ", "o", " "], [" ", " ", " "]]
        self.tictactoe = Board()

    def test_initialization(self):
        self.assertEqual(self.tictactoe.current_player, "x")

    def test_make_not_valid_move(self):
        self.tictactoe.board = self.mock_board
        row, col = 0, 0
        move = self.tictactoe.make_move(row, col, "o")
        self.assertFalse(move)

    def test_valid_move(self):
        self.tictactoe.board = self.mock_board
        row, col = 2, 1
        is_valid = self.tictactoe.is_valid_move(row, col)
        self.assertTrue(is_valid)

    def test_not_valid_move(self):
        self.tictactoe.board = self.mock_small_board
        row, col = 0, 0
        is_valid = self.tictactoe.is_valid_move(row, col)
        self.assertFalse(is_valid)

    def test_get_current_player(self):
        self.tictactoe.current_player = "x"
        current = self.tictactoe.get_current_player()
        self.assertEqual(self.tictactoe.current_player, current)

    def test_is_game_over_false(self):
        self.tictactoe.board = self.mock_board
        self.tictactoe.board[0][0] = "x"
        last_move = (0, 0)
        result = self.tictactoe.is_game_over(last_move)
        self.assertFalse(result)

    def test_is_game_over_true_draw(self):
        game = Board(size=3)
        self.tictactoe.board = [["x", "x", "o"], ["o", "o", "x"], ["x", "o", "x"]]
        last_move = (0, 0)
        game.turn = 9
        result = game.is_game_over(last_move)
        self.assertTrue(result)

    @patch("ai.Minimax.check_winner")
    def test_is_game_over_true_win(self, mock_minimax):
        last_move = (0, 0)
        mock_minimax.return_value = True
        result = self.tictactoe.is_game_over(last_move)
        self.assertTrue(result)

    def test_print_board_3x3(self):
        game = Board(size=3)
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
            game.print_board()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()

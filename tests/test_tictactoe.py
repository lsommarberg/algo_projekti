import unittest
from unittest.mock import patch
import io
from tic_tac_toe import TicTacToe


class TestGame(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()
        self.mock_board = [[" " for _ in range(20)] for _ in range(20)]
        self.mock_board[0][0] = "x"
        self.mock_small_board = [["x", " ", " "], [" ", "o", " "], [" ", " ", " "]]

    def test_initialization(self):
        self.assertEqual(self.tictactoe.current_player, "x")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_board(self, mock_stdout):
        self.tictactoe.board = self.mock_small_board
        self.tictactoe.display_board()

        printed_output = mock_stdout.getvalue()
        expected_output = "['x', ' ', ' ']\n[' ', 'o', ' ']\n[' ', ' ', ' ']\n"

        self.assertEqual(printed_output, expected_output)

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

    def test_check_winner_true_x(self):
        mock_board = [[" " for _ in range(20)] for _ in range(20)]
        for i in range(4, 9):
            mock_board[-i][i] = "o"
        for i in range(4, 9):
            mock_board[i][3] = "x"

        winner = self.tictactoe.check_winner(mock_board, "x", (5, 3))
        self.assertTrue(winner)

    def test_check_winner_false_x(self):
        mock_board = [[" " for _ in range(20)] for _ in range(20)]
        for i in range(4, 9):
            mock_board[-i][i] = "o"

        mock_board[5][3] = "x"

        winner = self.tictactoe.check_winner(mock_board, "x", (5, 3))
        self.assertFalse(winner)

    def test_update_possible_moves(self):
        mock_board = [[" " for _ in range(5)] for _ in range(5)]
        mock_last_move = (0, 0)
        mock_board[0][0] = "x"
        updated_moves = self.tictactoe.update_possible_moves(
            mock_board, mock_last_move, possible_moves=[]
        )
        expected_output = [
            (0, 1),
            (0, 2),
            (1, 1),
            (1, 2),
            (1, 0),
            (2, 2),
            (2, 0),
            (2, 1),
        ]
        for move in updated_moves:
            self.subTest(move=move)
            self.assertIn(move, expected_output)

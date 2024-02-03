import unittest
from unittest.mock import patch
import io
from tic_tac_toe import TicTacToe


class TestGame(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()
        self.mock_board = [["x", " ", " "], [" ", "o", " "], [" ", " ", " "]]
        self.mock_draw = [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]
        self.mock_winner_x = [["x", "x", "x"], ["o", " ", " "], ["o", "x", "o"]]
        self.mock_winner_o = [["x", " ", "o"], ["x", "o", "x"], ["o", "x", "o"]]

    def test_initialization(self):
        self.assertEqual(self.tictactoe.current_player, "x")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display_board(self, mock_stdout):
        self.tictactoe.board = self.mock_board
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
        row, col = 1, 1
        is_valid = self.tictactoe.is_valid_move(row, col)
        self.assertFalse(is_valid)

    def test_switch_player(self):
        self.tictactoe.current_player = "x"
        self.tictactoe.switch_player()
        self.assertEqual(self.tictactoe.current_player, "o")

    def test_check_draw_true(self):
        self.tictactoe.board = self.mock_draw
        draw = self.tictactoe.check_draw(self.tictactoe.board)
        self.assertTrue(draw)

    def test_check_draw_false(self):
        self.tictactoe.board = self.mock_winner_x
        draw = self.tictactoe.check_draw(self.tictactoe.board)
        self.assertFalse(draw)

    def test_check_winner_true_x(self):
        winner = self.tictactoe.check_winner(self.mock_winner_x, "x")
        self.assertTrue(winner)

    def test_check_winner_false_x(self):
        winner = self.tictactoe.check_winner(self.mock_draw, "x")
        self.assertFalse(winner)

    def test_check_winner_wrong_symbol(self):
        winner = self.tictactoe.check_winner(self.mock_winner_x, "o")
        self.assertFalse(winner)

    def test_check_winner_o(self):
        winner = self.tictactoe.check_winner(self.mock_winner_o, "o")
        self.assertTrue(winner)

    @patch("ai.TicTacToe.is_valid_move")
    def test_make_valid_move(self, is_valid_move_mock):
        self.tictactoe.board = self.mock_board
        self.tictactoe.current_player = "x"
        row, col = 1, 2
        is_valid_move_mock.return_value = True
        self.tictactoe.make_move(row, col)
        expected_output = [["x", " ", " "], [" ", "o", "x"], [" ", " ", " "]]
        move = self.tictactoe.board
        self.assertEqual(expected_output, move)

    @patch("ai.TicTacToe.is_valid_move")
    def test_make_not_valid_move(self, is_valid_move_mock):
        self.tictactoe.board = self.mock_board
        self.tictactoe.current_player = "x"
        row, col = 1, 1
        is_valid_move_mock.return_value = False
        move = self.tictactoe.make_move(row, col)
        self.assertFalse(move)

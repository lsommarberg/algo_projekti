import unittest
from unittest.mock import patch
import io
from ai import TicTacToeAI, State, TicTacToe


class TestGame(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToeAI()
        self.mock_board = [["x", " ", " "], [" ", "o", " "], [" ", " ", " "]]
        self.mock_draw = [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]]
        self.mock_winner_x = [["x", "x", "x"], ["o", " ", " "], ["o", "x", "o"]]
        self.mock_winner_o = [["o", "o", "o"], ["x", " ", "x"], ["x", "x", " "]]
        self.mock_state_draw = State(self.mock_draw, "o", (0, 1))
        self.mock_state_winner_x = State(self.mock_winner_x, "o", (0, 1))
        self.mock_state_winner_o = State(self.mock_winner_o, "o", (0, 1))
        self.mock_state = State(self.mock_winner_x, "x", (0, 1))

    def test_is_terminal_state_true(self):
        mock_state = State(
            [["x", "o", "x"], ["o", "x", "o"], ["o", "x", "o"]], "o", (1, 2)
        )
        is_terminal = State.is_terminal_state(mock_state)
        self.assertTrue(is_terminal)

    def test_is_terminal_state_false(self):
        mock_state = State(
            [["x", "o", "x"], [" ", " ", "o"], ["o", "x", "o"]], "o", (1, 2)
        )
        is_terminal = State.is_terminal_state(mock_state)
        self.assertFalse(is_terminal)

    @patch("ai.TicTacToeAI.max_value")
    @patch("ai.State.children")
    def test_ai_make_move(self, mock_children, mock_minimax):
        mock_children.return_value = [State(self.mock_board, "o", (1, 1))]
        mock_minimax.return_value = 42

        result = self.tictactoe.ai_make_move(self.mock_board)

        self.assertEqual(result, (1, 1))
        mock_children.assert_called_once()
        mock_minimax.assert_called_once_with(
            mock_children.return_value[0], depth=3, alpha=-10000, beta=10000
        )

    @patch("ai.TicTacToe.check_winner")
    @patch("ai.TicTacToe.check_draw")
    def test_is_terminal_state_winner(self, mock_winner, mock_draw):
        mock_draw.return_value = False
        mock_winner.return_value = True
        result = self.mock_state_winner_x.is_terminal_state()
        self.assertEqual(result, True)

    @patch("ai.TicTacToe.check_draw")
    def test_is_terminal_state_draw(self, mock_draw):
        mock_draw.return_value = True
        result = self.mock_state_draw.is_terminal_state()
        self.assertEqual(result, True)

    @patch("ai.TicTacToe.check_draw")
    def test_evaluate_draw(self, mock_draw):
        mock_draw.return_value = True
        result = self.tictactoe.evaluate(self.mock_state_draw)
        self.assertEqual(result, 0)

    @patch("ai.TicTacToe.check_winner")
    def test_evaluate_winner_x(self, mock_winner):
        mock_winner.return_value = True
        result = self.tictactoe.evaluate(self.mock_state_winner_x)
        self.assertEqual(result, -10)

    def test_evaluate_winner_o(self):
        result = self.tictactoe.evaluate(self.mock_state_winner_o)
        self.assertEqual(result, 10)

    def test_children(self):
        result = self.mock_state.children()
        self.assertEqual(len(result), 2)

from tic_tac_toe import TicTacToeGame, Board, Minimax
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()
        self.mock_board = Board()
        self.mock_minimax = Minimax()
        self.mock_input = MagicMock(side_effect=["1", "100"])

    @patch("builtins.input", side_effect=["5", "7"])
    def test_human_move_valid(self, mock_input):
        game = TicTacToeGame()
        game.board.board = [[" " for _ in range(20)] for _ in range(20)]

        game.human_move()

        self.assertEqual(game.board.board[4][6], "x")
        self.assertEqual((4, 6), game.minimax.last_move)
        self.assertEqual(game.board.current_player, "o")

    @patch("builtins.input", side_effect=["5", "7"])
    def test_human_move_not_valid(self, mock_input):
        game = TicTacToeGame()
        game.board.board = [[" " for _ in range(20)] for _ in range(20)]
        game.board.board[4][6] = "x"
        self.assertIsNone(game.minimax.last_move)

    def test_ai_move(self):
        game = TicTacToeGame()
        mock_minimax = MagicMock()
        game.board.board = [["x", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        game.board.turn = 1
        expected_board_state = [["x", " ", " "], [" ", " ", "o"], [" ", " ", " "]]
        with patch.object(game, "minimax", mock_minimax):
            row = 1
            col = 2
            mock_minimax.get_best_move.return_value = (row, col)

            game.ai_move()
            mock_minimax.update_board_state.assert_called_once_with(
                (row, col), expected_board_state
            )
            self.assertEqual(game.board.current_player, "x")

    def test_start_game(self):
        game = TicTacToeGame()
        game.board = MagicMock()
        game.board.size = 3

        game.human_move = MagicMock(
            side_effect=[(0, 1), (0, 0), (1, 2), (2, 2), (2, 0)]
        )
        game.ai_move = MagicMock(side_effect=[(1, 2), (1, 1), (1, 0), (2, 1)])

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            game.start()

            printed_output = mock_stdout.getvalue()

        expected_output = "Game Over"

        self.assertEqual(printed_output.strip(), expected_output.strip())

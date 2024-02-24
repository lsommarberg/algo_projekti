import unittest
from unittest.mock import MagicMock
from ai import Minimax


class TestGame(unittest.TestCase):
    def setUp(self):
        self.minimax = Minimax()

    def test_check_winner_true_x(self):
        mock_board = [[" " for _ in range(20)] for _ in range(20)]
        for i in range(4, 9):
            mock_board[-i][i] = "o"
        for i in range(4, 9):
            mock_board[i][3] = "x"

        winner = self.minimax.check_winner(mock_board, "x", (5, 3))
        self.assertTrue(winner)

    def test_check_winner_false_x(self):
        mock_board = [[" " for _ in range(20)] for _ in range(20)]
        for i in range(4, 9):
            mock_board[-i][i] = "o"

        mock_board[5][3] = "x"

        winner = self.minimax.check_winner(mock_board, "x", (5, 3))
        self.assertFalse(winner)

    def test_update_possible_moves(self):
        mock_board = [[" " for _ in range(5)] for _ in range(5)]
        mock_last_move = (0, 0)
        mock_board[0][0] = "x"
        updated_moves = self.minimax.update_possible_moves(
            mock_board,
            mock_last_move,
            possible_moves=[
                (0, 1),
                (0, 2),
                (1, 1),
                (1, 2),
                (1, 0),
                (2, 2),
                (2, 0),
                (2, 1),
            ],
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

    def test_update_possible_moves_2(self):
        mock_board = [
            ["o", " ", " ", " ", " ", " ", " ", " ", "x", "o"],
            ["o", "x", "o", "x", "o", "o", "o", "x", "o", "o"],
            ["x", "o", "x", "x", "x", "o", "o", "o", " ", " "],
            ["o", "x", "x", "o", "x", "o", "x", "x", "x", "x"],
            ["o", "x", "o", "x", "o", "x", "x", "x", "x", " "],
            ["x", "o", "o", "x", "x", "o", "o", "x", "o", " "],
            ["x", "x", "o", "o", "o", "o", "x", "x", "x", "x"],
            ["x", "o", "x", "x", "x", "o", "o", "o", "x", "o"],
            ["o", "o", "x", "o", "x", "o", "x", "o", "o", "o"],
            ["x", "x", "x", "o", "o", "x", "o", "o", "o", "x"],
        ]

        mock_last_move = (0, 0)
        updated_moves = self.minimax.update_possible_moves(
            mock_board,
            mock_last_move,
            possible_moves=[
                (0, 1),
                (0, 2),
                (0, 3),
                (0, 4),
                (0, 5),
                (0, 6),
                (0, 7),
                (2, 8),
                (2, 9),
                (4, 9),
                (5, 9),
            ],
        )
        expected_output = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (0, 6),
            (0, 7),
            (2, 8),
            (2, 9),
            (4, 9),
            (5, 9),
        ]

        for move in updated_moves:
            self.subTest(move=move)
            self.assertIn(move, expected_output)

    def test_minimax_stop_opponent(self):
        board = [["o", " ", "x"], ["x", "o", " "], [" ", " ", "x"]]
        mock_tictactoe = Minimax()
        moves = [(1, 2), (0, 1), (2, 1), (2, 0)]
        last_move = (2, 2)
        expected_move = (1, 2)

        _, actual_move = mock_tictactoe.minimax(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            count=5,
            max_player=True,
        )

        self.assertEqual(actual_move, expected_move)

    def test_minimax_ai_win(self):
        board = [["o", " ", "o"], ["x", "x", " "], [" ", " ", "x"]]

        mock_tictactoe = Minimax()
        moves = [(0, 1), (2, 1), (1, 2), (2, 0)]
        last_move = (1, 1)
        expected_move = (0, 1)
        _, actual_move = mock_tictactoe.minimax(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            count=5,
            max_player=True,
        )

        self.assertEqual(actual_move, expected_move)

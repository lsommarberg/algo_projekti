import unittest
from unittest.mock import patch
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

    def test_check_winner_diagonal_true(self):
        mock_board = [[" " for _ in range(10)] for _ in range(10)]
        for i in range(3, 8):
            mock_board[i][i - 1] = "o"

        winner = self.minimax.check_winner(mock_board, "o", (4, 3))
        self.assertTrue(winner)

    def test_check_winner_counter_diagonal_true(self):
        mock_board = [[" " for _ in range(10)] for _ in range(10)]
        for i in range(5, 10):
            mock_board[-i][i] = "o"

        winner = self.minimax.check_winner(mock_board, "o", (3, 7))
        self.assertTrue(winner)

    def test_check_winner_row_true(self):
        mock_board = [[" " for _ in range(10)] for _ in range(10)]
        for i in range(3, 8):
            mock_board[3][i] = "o"

        winner = self.minimax.check_winner(mock_board, "o", (3, 3))
        self.assertTrue(winner)

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
        self.assertEqual(len(expected_output), len(updated_moves))

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
            turn=5,
            max_player=True,
        )

        self.assertEqual(actual_move, expected_move)

    def test_minimax_draw(self):
        board = [["o", "x", "o"], ["x", "o", "x"], ["x", " ", "x"]]
        mock_tictactoe = Minimax(size=3)
        moves = [(2, 1)]
        last_move = (2, 2)
        expected_move = (2, 1)

        value, actual_move = mock_tictactoe.minimax(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            turn=8,
            max_player=True,
        )
        self.assertEqual(value, 0)
        self.assertEqual(actual_move, expected_move)

    def test_minimax_ai_win(self):
        board = [[" " for _ in range(5)] for _ in range(5)]

        for i in range(2, 5):
            board[i][2] = "o"

        for i in range(2, 5):
            board[i][3] = "x"

        board[0][2] = "o"
        board[0][3] = "x"

        mock_tictactoe = Minimax()
        moves = [
            (0, 1),
            (0, 4),
            (1, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 1),
            (2, 4),
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, 1),
            (3, 4),
            (4, 0),
            (4, 1),
            (4, 4),
        ]
        last_move = (0, 3)
        expected_move = (1, 2)
        _, actual_move = mock_tictactoe.minimax(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            turn=5,
            max_player=True,
        )

        self.assertEqual(actual_move, expected_move)

    @patch("ai.Minimax.minimax")
    def test_get_best_move(self, minimax):
        minimax.return_value = None, (1, 2)
        board = [["o", " ", "x"], ["x", "o", " "], [" ", " ", "x"]]
        mock_tictactoe = Minimax()
        mock_tictactoe.last_move = (2, 2)
        mock_tictactoe.possible_moves = [(1, 2), (0, 1), (2, 1), (2, 0)]
        expected_move = (1, 2)
        actual_move = mock_tictactoe.get_best_move(board, turn=5)

        self.assertEqual(actual_move, expected_move)

    def test_update_board_state(self):
        mock_tictactoe = Minimax(size=3)
        board = [["o", " ", "x"], ["x", "o", " "], [" ", " ", "x"]]
        mock_tictactoe = Minimax()
        last_move = (2, 2)
        mock_tictactoe.possible_moves = [(1, 2), (2, 2), (0, 1), (2, 1), (2, 0)]

        mock_tictactoe.update_board_state(last_move, board)
        self.assertEqual(last_move, mock_tictactoe.last_move)

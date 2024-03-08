import unittest
from ai import Minimax, Heuristic


class TestHeuristic(unittest.TestCase):
    def setUp(self):
        self.minimax = Minimax()

    def test_evaluate_c_diag(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[-i][i] = "o"

        move = (4, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_c_diag(board, move, symbol="o")
        expected_score = 50
        self.assertEqual(score, expected_score)

    def test_evaluate_diag(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[i + 1][i] = "o"

        move = (7, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_diag(board, move, symbol="o")
        expected_score = 50
        self.assertEqual(score, expected_score)

    def test_evaluate_diag_false(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(6, 8):
            board[i + 1][i] = "o"

        move = (7, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_diag(board, move, symbol="o")
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_evaluate_c_diag_false(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(6, 8):
            board[-i][i] = "o"

        move = (4, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_c_diag(board, move, symbol="o")
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_evaluate_row(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[3][i] = "o"

        move = (3, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_row(board, move, symbol="o")
        expected_score = 50
        self.assertEqual(score, expected_score)

    def test_evaluate_row_false(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(6, 8):
            board[3][i] = "o"

        move = (3, 6)
        mock_heuristic = Heuristic()
        score = mock_heuristic.evaluate_row(board, move, symbol="o")
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_evaluate_row_false(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(6, 8):
            board[3][i] = "o"

        move = (3, 6)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_row(board, move, symbol="o")
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_evaluate_col(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[i][3] = "o"

        move = (5, 3)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_col(board, move, symbol="o")
        expected_score = 50
        self.assertEqual(score, expected_score)

    def test_evaluate_col_false(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 7):
            board[i][3] = "o"

        move = (5, 3)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_col(board, move, symbol="o")
        expected_score = 0
        self.assertEqual(score, expected_score)

    def test_evaluate_col_block(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[i][3] = "x"

        board[4][3] = "o"

        move = (4, 3)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_col(board, move, symbol="o")
        expected_score = 30
        self.assertEqual(score, expected_score)

    def test_evaluate_row_block(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[3][i] = "x"

        board[3][4] = "o"

        move = (3, 4)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_row(board, move, symbol="o")
        expected_score = 30
        self.assertEqual(score, expected_score)

    def test_evaluate_diag_block(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[i + 1][i] = "x"

        board[5][4] = "o"

        move = (5, 4)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_diag(board, move, symbol="o")
        expected_score = 30
        self.assertEqual(score, expected_score)

    def test_evaluate_c_diag_block(self):
        board = [[" " for _ in range(10)] for _ in range(10)]

        for i in range(5, 8):
            board[-i][i] = "x"

        board[2][8] = "o"

        move = (2, 8)
        mock_heuristic = Heuristic(self.minimax)
        score = mock_heuristic.evaluate_c_diag(board, move, symbol="o")
        expected_score = 30
        self.assertEqual(score, expected_score)

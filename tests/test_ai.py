import unittest
from unittest.mock import MagicMock
from tic_tac_toe import TicTacToe
from ai import Minimax


class TestGame(unittest.TestCase):


    def test_minimax_stop_opponent(self):

        board = [["o", " ", "x"], 
                 ["x", "o", " "], 
                 [" ", " ", "x"]]
        mock_tictactoe = Minimax(size=3)
        mock_tictactoe.board = board
        moves = [(0, 1), (2, 1), (2, 0), (1, 2)]
        last_move = (2, 2)
        expected_move = (1, 2)

        _, actual_move = mock_tictactoe.max_value(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            count=5
        )

        self.assertEqual(actual_move, expected_move)

    
    def test_minimax_ai_win(self):
        board = [["o", " ", "o"], 
                 ["x", "x", " "], 
                 [" ", " ", "x"]]
        
        mock_tictactoe = Minimax(size=3)
        mock_tictactoe.board = board
        moves = [(2, 1), (1, 2), (2, 0), (0, 1)]
        last_move = (1, 1)
        expected_move = (0, 1)
        _, actual_move = mock_tictactoe.max_value(
            board,
            depth=3,
            alpha=-1000000,
            beta=1000000,
            moves=moves,
            last_move=last_move,
            count=5
        )

        self.assertEqual(actual_move, expected_move)

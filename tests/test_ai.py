import unittest
from unittest.mock import patch
import io
from tic_tac_toe import TicTacToe
from ai import evaluate


class TestGame(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()


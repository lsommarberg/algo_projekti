from tic_tac_toe import TicTacToeGame
import unittest
from unittest.mock import patch
from io import StringIO
import sys


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

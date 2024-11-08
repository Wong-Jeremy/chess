""" This module runs tests for the Pawn class """

import unittest
from src.pawn import Pawn
from src.board import Board


class TestPawn(unittest.TestCase):
    """
    Run tests for the Pawn class.
    """

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        pawn = Pawn('W', (1, 1)) # A pawn on B2
        self.assertEqual(pawn.get_colour(), 'W')
        self.assertEqual(pawn.pos, (1, 1))


    def test_non_captures(self):
        """
        Ensure that get_all_moves_returns only non-captures
        """

        board = Board()
        pawn = Pawn('W', (1, 1))
    
        

if __name__ == '__main__':
    unittest.main()
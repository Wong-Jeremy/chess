""" This module runs tests for the Knight class """

import unittest
from src.knight import Knight
from src.pawn import Pawn
from src.piece import BasicPiece
from src.board import Board

class TestKnight(unittest.TestCase):
    """
    Run tests for the Knight class.
    """

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        knight = Knight('W', (3, 3)) # A knight on D4
        self.assertEqual(knight.get_colour(), 'W')
        self.assertEqual(knight.get_piece_type(), 'knight')
        self.assertEqual(knight.get_starting_square(), (3, 3))
        self.assertEqual(knight.pos, (3, 3))

    def test_non_captures(self):
        """
        Ensure that all non-capturing moves are found
        """

        board = Board()

        # A knight in the middle of the board
        knight = board.add_piece(Knight('W', (3, 3))) # A knight on D4
        knight.update_all_moves(board)
        all_moves = knight.all_moves

        self.assertEqual(len(all_moves), 8)
        self.assertIn(((4, 5), 'N'), all_moves)
        self.assertIn(((5, 4), 'N'), all_moves)
        self.assertIn(((5, 2), 'N'), all_moves)
        self.assertIn(((4, 1), 'N'), all_moves)
        self.assertIn(((2, 1), 'N'), all_moves)
        self.assertIn(((1, 2), 'N'), all_moves)
        self.assertIn(((1, 4), 'N'), all_moves)
        self.assertIn(((2, 5), 'N'), all_moves)

        # A knight on the edge of the board
        knight_2 = board.add_piece(Knight('W', (1, 7))) # A knight on B8
        knight_2.update_all_moves(board)
        all_moves = knight_2.all_moves
        self.assertEqual(len(all_moves), 3)
        self.assertIn(((0, 5), 'N'), all_moves)
        self.assertIn(((2, 5), 'N'), all_moves)
        self.assertIn(((3, 6), 'N'), all_moves)

    def test_captures(self):
        """
        Ensure that all non-capturing and capturing moves are found
        """

        board = Board()

        # A knight in the middle of the board
        knight = board.add_piece(Knight('W', (3, 3))) # A white knight on D4
        pawn_1 = board.add_piece(Pawn('W', (1, 2))) # A white pawn on B3
        pawn_2 = board.add_piece(Pawn('W', (2, 1))) # A white pawn on C2
        pawn_3 = board.add_piece(Pawn('B', (4, 1))) # A black pawn on E2
        pawn_4 = board.add_piece(Pawn('B', (5, 2))) # A black pawn on E2

        knight.update_all_moves(board)
        all_moves = knight.all_moves

        self.assertEqual(len(all_moves), 6)
        self.assertIn(((1, 4), 'N'), all_moves)
        self.assertIn(((2, 5), 'N'), all_moves)
        self.assertIn(((4, 5), 'N'), all_moves)
        self.assertIn(((5, 4), 'N'), all_moves)

        self.assertIn(((5, 2), 'C'), all_moves)
        self.assertIn(((4, 1), 'C'), all_moves)



if __name__ == '__main__':
    unittest.main()
""" This module runs tests for the Bishop class """

import unittest
from src.bishop import Bishop
from src.pawn import Pawn
from src.piece import BasicPiece
from src.board import Board


class TestBishop(unittest.TestCase):
    """
    Run tests for the Bishop class.
    """

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        bishop = Bishop('W', (0, 1)) # A bishop on A2
        self.assertEqual(bishop.get_colour(), 'W')
        self.assertEqual(bishop.pos, (0, 1))


    def test_non_captures(self):
        """
        Ensure that get_all_moves returns only non-captures on empty board
        """

        board = Board()
        # Bishop on the rim
        bishop = board.add_piece(Bishop('W', (0, 1))) # A bishop on A2

        bishop.update_all_moves(board)
        all_moves = bishop.all_moves

        self.assertEqual(len(all_moves), 7)
        self.assertIn(((1, 0), "N"), all_moves)
        self.assertIn(((1, 2), "N"), all_moves)
        self.assertIn(((2, 3), "N"), all_moves)
        self.assertIn(((3, 4), "N"), all_moves)
        self.assertIn(((4, 5), "N"), all_moves)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((6, 7), "N"), all_moves)

        board.remove_piece_by_square((0, 1))

        # Bishop in the middle of the board
        bishop = board.add_piece(Bishop('B', (3, 3))) # A bishop on D4
        bishop.update_all_moves(board)
        all_moves = bishop.all_moves

        self.assertEqual(len(all_moves), 13)
        self.assertIn(((0, 0), "N"), all_moves)
        self.assertIn(((1, 1), "N"), all_moves)
        self.assertIn(((2, 2), "N"), all_moves)

        self.assertIn(((4, 4), "N"), all_moves)
        self.assertIn(((5, 5), "N"), all_moves)
        self.assertIn(((6, 6), "N"), all_moves)
        self.assertIn(((7, 7), "N"), all_moves)

        self.assertIn(((4, 2), "N"), all_moves)
        self.assertIn(((5, 1), "N"), all_moves)
        self.assertIn(((6, 0), "N"), all_moves)

        self.assertIn(((2, 4), "N"), all_moves)
        self.assertIn(((1, 5), "N"), all_moves)
        self.assertIn(((0, 6), "N"), all_moves)

        board.remove_piece_by_square((3, 3))

        # Bishop blocked by pawns
        bishop = board.add_piece(Bishop('W', (5, 0))) # A white bishop on F1
        pawn_1 = board.add_piece(Pawn('W', (4, 1))) # A white pawn on E2
        pawn_2 = board.add_piece(Pawn('W', (6, 1))) # A white pawn on G2
        bishop.update_all_moves(board)
        all_moves = bishop.all_moves

        self.assertTrue(len(all_moves) == 0)


    def test_captures(self):
        """
        Ensure that get_all_moves returns captures and non-captures on empty board
        """

        board = Board()

        bishop = board.add_piece(Bishop('B', (6, 6))) # A black bishop on G7
        pawn_1 = board.add_piece(Pawn('W', (4, 4))) # A white pawn on E5
        pawn_2 = board.add_piece(Pawn('W', (7, 5))) # A white pawn on H6

        bishop.update_all_moves(board)
        all_moves = bishop.all_moves

        self.assertTrue(len(all_moves) == 5)
        self.assertIn(((4, 4), "C"), all_moves)
        self.assertIn(((7, 5), "C"), all_moves)

        self.assertIn(((5, 5), "N"), all_moves)
        self.assertIn(((5, 7), "N"), all_moves)
        self.assertIn(((7, 7), "N"), all_moves)

    def test_squares_defended(self):
        """
        Ensure that get_all_moves_returns the squares_defended field is updated on get_all_moves
        This test is near identical to the previous but focusses on squares_defended only
        """

        board = Board()

        bishop = board.add_piece(Bishop('B', (6, 6))) # A black bishop on G7
        pawn_1 = board.add_piece(Pawn('B', (4, 4))) # A black pawn on E5
        pawn_2 = board.add_piece(Pawn('W', (7, 5))) # A white pawn on H6

        bishop.update_all_moves(board)
        squares_defended = bishop.squares_defended

        self.assertTrue(len(squares_defended) == 5)
        self.assertIn(((4, 4)), squares_defended)
        self.assertIn(((5, 5)), squares_defended)
        self.assertIn(((7, 7)), squares_defended)
        self.assertIn(((5, 7)), squares_defended)
        self.assertIn(((7, 5)), squares_defended)


    def test_x_ray_pieces(self):
        """
        Ensure that pieces x_ray pieces are marked appropriately
        """

        board = Board()

        bishop = board.add_piece(Bishop('B', (6, 6))) # A black bishop on G7
        pawn = board.add_piece(Pawn('W', (4, 4))) # A white pawn on E5
        # King class currently not implemented so just using BasicPiece instantiation
        king = board.add_piece(BasicPiece('W', 'king', (1, 1))) # A white king on B2

        bishop.update_all_moves(board)
        all_moves = bishop.all_moves

        self.assertTrue(len(all_moves) == 5)
        self.assertIn(((4, 4), "C"), all_moves)

        self.assertIn(((7, 5), "N"), all_moves)
        self.assertIn(((5, 5), "N"), all_moves)
        self.assertIn(((5, 7), "N"), all_moves)
        self.assertIn(((7, 7), "N"), all_moves)

        self.assertTrue(pawn.is_pinned)
        pinned_squares = pawn.pinned_squares
        self.assertEqual(len(pinned_squares), 4)
        self.assertIn((6, 6), pinned_squares)
        self.assertIn((5, 5), pinned_squares)
        self.assertIn((3, 3), pinned_squares)
        self.assertIn((2, 2), pinned_squares)




if __name__ == '__main__':
    unittest.main()
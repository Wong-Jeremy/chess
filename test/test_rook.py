""" This module runs tests for the Rook class """

import unittest
from src.rook import Rook
from src.pawn import Pawn
from src.piece import BasicPiece
from src.board import Board

class TestRook(unittest.TestCase):
    """
    Run tests for the Bishop class.
    """

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        rook = Rook('W', (0, 0)) # A rook on A1
        self.assertEqual(rook.get_colour(), 'W')
        self.assertEqual(rook.pos, (0, 0))


    def test_non_captures(self):
        """
        Ensure that get_all_moves returns only non-captures on empty board
        """

        board = Board()
        # rook on the rim
        rook = board.add_piece(Rook('W', (0, 0))) # A rook on A1

        rook.update_all_moves(board)
        all_moves = rook.all_moves

        self.assertEqual(len(all_moves), 14)
        for i in range(1, 8):
            with self.subTest(i=i):
                self.assertIn(((0, i), "N"), all_moves)
                self.assertIn(((i, 0), "N"), all_moves)


        board.remove_piece_by_square((0, 0))

        # Rook in the middle of the board
        rook = board.add_piece(Rook('B', (3, 3))) # A rook on D4
        rook.update_all_moves(board)
        all_moves = rook.all_moves

        self.assertEqual(len(all_moves), 14)
        self.assertIn(((3, 0), "N"), all_moves)
        self.assertIn(((3, 1), "N"), all_moves)
        self.assertIn(((3, 2), "N"), all_moves)

        self.assertIn(((3, 4), "N"), all_moves)
        self.assertIn(((3, 5), "N"), all_moves)
        self.assertIn(((3, 6), "N"), all_moves)
        self.assertIn(((3, 7), "N"), all_moves)

        self.assertIn(((0, 3), "N"), all_moves)
        self.assertIn(((1, 3), "N"), all_moves)
        self.assertIn(((2, 3), "N"), all_moves)

        self.assertIn(((4, 3), "N"), all_moves)
        self.assertIn(((5, 3), "N"), all_moves)
        self.assertIn(((6, 3), "N"), all_moves)
        self.assertIn(((7, 3), "N"), all_moves)

        board.remove_piece_by_square((3, 3))

        # Rook blocked by pawns
        rook = board.add_piece(Rook('W', (1, 3))) # A white rook on B4
        pawn_1 = board.add_piece(Pawn('W', (1, 4))) # A white pawn on B5
        pawn_2 = board.add_piece(Pawn('W', (2, 3))) # A white pawn on C4
        rook.update_all_moves(board)
        all_moves = rook.all_moves

        self.assertTrue(len(all_moves) == 4)
        self.assertIn(((1, 2), "N"), all_moves)
        self.assertIn(((1, 1), "N"), all_moves)
        self.assertIn(((1, 0), "N"), all_moves)

        self.assertIn(((0, 3), "N"), all_moves)


    def test_captures(self):
        """
        Ensure that get_all_moves returns captures and non-captures on empty board
        """

        board = Board()
        # Rook in the middle of the board
        rook = board.add_piece(Rook('B', (5, 5))) # A black rook on F6
        pawn_1 = board.add_piece(Pawn('W', (1, 5))) # A white pawn on B6
        pawn_2 = board.add_piece(Pawn('W', (5, 1))) # A white pawn on F2
        pawn_3 = board.add_piece(Pawn('B', (6, 5))) # A black pawn on G6
        rook.update_all_moves(board)
        all_moves = rook.all_moves

        self.assertEqual(len(all_moves), 10)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((5, 7), "N"), all_moves)

        self.assertIn(((5, 4), "N"), all_moves)
        self.assertIn(((5, 3), "N"), all_moves)
        self.assertIn(((5, 2), "N"), all_moves)
        self.assertIn(((5, 1), "C"), all_moves)

        self.assertIn(((4, 5), "N"), all_moves)
        self.assertIn(((3, 5), "N"), all_moves)
        self.assertIn(((2, 5), "N"), all_moves)
        self.assertIn(((1, 5), "C"), all_moves)


    def test_squares_defended(self):
        """
        Ensure that get_all_moves_returns the squares_defended field is updated on get_all_moves
        This test is near identical to the previous but focusses on squares_defended only
        """

        board = Board()
        # Rook in the middle of the board
        rook = board.add_piece(Rook('B', (5, 5))) # A black rook on F6
        pawn_1 = board.add_piece(Pawn('W', (1, 5))) # A white pawn on B6
        pawn_2 = board.add_piece(Pawn('W', (5, 1))) # A white pawn on F2
        pawn_3 = board.add_piece(Pawn('B', (6, 5))) # A black pawn on G6

        rook.update_all_moves(board)
        squares_defended = rook.squares_defended

        self.assertEqual(len(squares_defended), 11)
        self.assertIn((5, 6), squares_defended)
        self.assertIn((5, 7), squares_defended)

        self.assertIn((6, 5), squares_defended)

        self.assertIn((5, 4), squares_defended)
        self.assertIn((5, 3), squares_defended)
        self.assertIn((5, 2), squares_defended)
        self.assertIn((5, 1), squares_defended)

        self.assertIn((4, 5), squares_defended)
        self.assertIn((3, 5), squares_defended)
        self.assertIn((2, 5), squares_defended)
        self.assertIn((1, 5), squares_defended)


    def test_x_ray_pieces(self):
        """
        Ensure that pieces x_ray pieces are marked appropriately
        """

        board = Board()

        rook = board.add_piece(Rook('B', (6, 6))) # A black rook on G7
        pawn = board.add_piece(Pawn('W', (6, 4))) # A white pawn on G5
        # King class currently not implemented so just using BasicPiece instantiation
        king = board.add_piece(BasicPiece('W', 'king', (6, 2))) # A white king on G3

        rook.update_all_moves(board)
        all_moves = rook.all_moves

        self.assertTrue(len(all_moves) == 10)
        self.assertIn(((6, 7), "N"), all_moves)

        self.assertIn(((7, 6), "N"), all_moves)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((4, 6), "N"), all_moves)
        self.assertIn(((3, 6), "N"), all_moves)
        self.assertIn(((2, 6), "N"), all_moves)
        self.assertIn(((1, 6), "N"), all_moves)
        self.assertIn(((0, 6), "N"), all_moves)

        self.assertIn(((6, 5), "N"), all_moves)
        self.assertIn(((6, 4), "C"), all_moves)

        self.assertTrue(pawn.is_pinned)
        pinned_squares = pawn.pinned_squares
        self.assertEqual(len(pinned_squares), 3)
        self.assertIn((6, 6), pinned_squares)
        self.assertIn((6, 5), pinned_squares)
        self.assertIn((6, 3), pinned_squares)


if __name__ == '__main__':
    unittest.main()
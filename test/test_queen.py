""" This module runs tests for the Queen class """

import unittest
from src.queen import Queen
from src.pawn import Pawn
from src.piece import BasicPiece
from src.board import Board


class TestQueen(unittest.TestCase):
    """
    Run tests for the Queen class.
    """

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        queen = Queen('W', (0, 1)) # A white queen on A2
        self.assertEqual(queen.get_colour(), 'W')
        self.assertEqual(queen.pos, (0, 1))


    def test_non_captures(self):
        """
        Ensure that get_all_moves returns only non-captures on empty board
        """

        board = Board()
        # Queen on the rim
        queen = board.add_piece(Queen('W', (0, 1))) # A white queen on A2

        queen.update_all_moves(board)
        all_moves = queen.all_moves

        self.assertEqual(len(all_moves), 21)

        self.assertIn(((1, 0), "N"), all_moves)

        self.assertIn(((1, 2), "N"), all_moves)
        self.assertIn(((2, 3), "N"), all_moves)
        self.assertIn(((3, 4), "N"), all_moves)
        self.assertIn(((4, 5), "N"), all_moves)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((6, 7), "N"), all_moves)

        self.assertIn(((0, 0), "N"), all_moves)
        self.assertIn(((0, 2), "N"), all_moves)
        self.assertIn(((0, 3), "N"), all_moves)
        self.assertIn(((0, 4), "N"), all_moves)
        self.assertIn(((0, 5), "N"), all_moves)
        self.assertIn(((0, 6), "N"), all_moves)
        self.assertIn(((0, 7), "N"), all_moves)

        self.assertIn(((1, 1), "N"), all_moves)
        self.assertIn(((2, 1), "N"), all_moves)
        self.assertIn(((3, 1), "N"), all_moves)
        self.assertIn(((4, 1), "N"), all_moves)
        self.assertIn(((5, 1), "N"), all_moves)
        self.assertIn(((6, 1), "N"), all_moves)
        self.assertIn(((7, 1), "N"), all_moves)

        board.remove_piece_by_square((0, 1))

        # Bishop in the middle of the board
        queen = board.add_piece(Queen('B', (3, 3))) # A queen on D4
        queen.update_all_moves(board)
        all_moves = queen.all_moves

        self.assertEqual(len(all_moves), 27)
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

        self.assertIn(((0, 0), "N"), all_moves)
        self.assertIn(((1, 1), "N"), all_moves)
        self.assertIn(((2, 2), "N"), all_moves)
        self.assertIn(((4, 4), "N"), all_moves)
        self.assertIn(((5, 5), "N"), all_moves)
        self.assertIn(((6, 6), "N"), all_moves)
        self.assertIn(((7, 7), "N"), all_moves)

        self.assertIn(((0, 6), "N"), all_moves)
        self.assertIn(((1, 5), "N"), all_moves)
        self.assertIn(((2, 4), "N"), all_moves)
        self.assertIn(((4, 2), "N"), all_moves)
        self.assertIn(((5, 1), "N"), all_moves)
        self.assertIn(((6, 0), "N"), all_moves)

        board.remove_piece_by_square((3, 3))

        # Queen around some pawns
        queen = board.add_piece(Queen('W', (5, 1))) # A white queen on F2
        pawn_1 = board.add_piece(Pawn('W', (4, 2))) # A white pawn on E3
        pawn_2 = board.add_piece(Pawn('W', (5, 3))) # A white pawn on F4
        pawn_3 = board.add_piece(Pawn('W', (6, 2))) # A white pawn on G3
        queen.update_all_moves(board)
        all_moves = queen.all_moves

        self.assertTrue(len(all_moves) == 11)

        self.assertIn(((0, 1), "N"), all_moves)
        self.assertIn(((1, 1), "N"), all_moves)
        self.assertIn(((2, 1), "N"), all_moves)
        self.assertIn(((3, 1), "N"), all_moves)
        self.assertIn(((4, 1), "N"), all_moves)
        self.assertIn(((6, 1), "N"), all_moves)
        self.assertIn(((7, 1), "N"), all_moves)

        self.assertIn(((5, 0), "N"), all_moves)
        self.assertIn(((5, 2), "N"), all_moves)

        self.assertIn(((4, 0), "N"), all_moves)
        self.assertIn(((6, 0), "N"), all_moves)


    def test_captures(self):
        """
        Ensure that get_all_moves returns captures and non-captures on board
        """

        board = Board()

        queen = board.add_piece(Queen('B', (1, 6))) # A black queen on B7
        pawn_1 = board.add_piece(Pawn('W', (1, 1))) # A white pawn on B2
        pawn_2 = board.add_piece(Pawn('W', (6, 1))) # A white pawn on G2
        pawn_3 = board.add_piece(Pawn('W', (6, 6))) # A white pawn on G7
        pawn_4 = board.add_piece(Pawn('B', (6, 1))) # A black pawn on D5

        queen.update_all_moves(board)
        all_moves = queen.all_moves

        self.assertTrue(len(all_moves) == 5)
        self.assertIn(((0, 7), "N"), all_moves)
        self.assertIn(((2, 5), "N"), all_moves)

        self.assertIn(((0, 6), "N"), all_moves)
        self.assertIn(((2, 6), "N"), all_moves)
        self.assertIn(((3, 6), "N"), all_moves)
        self.assertIn(((4, 6), "N"), all_moves)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((6, 6), "C"), all_moves)

        self.assertIn(((1, 7), "N"), all_moves)
        self.assertIn(((1, 5), "N"), all_moves)
        self.assertIn(((1, 4), "N"), all_moves)
        self.assertIn(((1, 3), "N"), all_moves)
        self.assertIn(((1, 2), "N"), all_moves)
        self.assertIn(((1, 1), "C"), all_moves)

        self.assertIn(((2, 7), "N"), all_moves)
        self.assertIn(((0, 5), "N"), all_moves)

    def test_squares_defended(self):
        """
        Ensure that get_all_moves_returns the squares_defended field is updated on get_all_moves
        This test is near identical to the previous but focusses on squares_defended only
        """

        board = Board()

        queen = board.add_piece(Queen('B', (2, 2))) # A black queen on C3
        pawn_1 = board.add_piece(Pawn('B', (1, 1))) # A black pawn on B2
        pawn_2 = board.add_piece(Pawn('B', (4, 4))) # A black pawn on E5
        pawn_3 = board.add_piece(Pawn('W', (6, 2))) # A white pawn on G3

        queen.update_all_moves(board)
        squares_defended = queen.squares_defended

        self.assertTrue(len(squares_defended) == 5)
        self.assertIn(((1, 1)), squares_defended)
        self.assertIn(((3, 3)), squares_defended)
        self.assertIn(((4, 4)), squares_defended)

        self.assertIn(((0, 2)), squares_defended)
        self.assertIn(((1, 2)), squares_defended)
        self.assertIn(((3, 2)), squares_defended)
        self.assertIn(((4, 2)), squares_defended)
        self.assertIn(((5, 2)), squares_defended)
        self.assertIn(((6, 2)), squares_defended)

        self.assertIn(((2, 0)), squares_defended)
        self.assertIn(((2, 1)), squares_defended)
        self.assertIn(((2, 3)), squares_defended)
        self.assertIn(((2, 4)), squares_defended)
        self.assertIn(((2, 5)), squares_defended)
        self.assertIn(((2, 6)), squares_defended)
        self.assertIn(((2, 7)), squares_defended)

        self.assertIn(((0, 4)), squares_defended)
        self.assertIn(((1, 3)), squares_defended)
        self.assertIn(((3, 1)), squares_defended)
        self.assertIn(((4, 0)), squares_defended)


    def test_x_ray_pieces(self):
        """
        Ensure that pieces x_ray pieces are marked appropriately
        """

        board = Board()

        queen = board.add_piece(Queen('B', (6, 6))) # A queen bishop on G7
        pawn_1 = board.add_piece(Pawn('W', (4, 4))) # A white pawn on E5
        pawn_2 = board.add_piece(Pawn('W', (3, 3))) # A white pawn on D4
        pawn_3 = board.add_piece(Pawn('W', (6, 4))) # A white pawn on G5
        # King class currently not implemented so just using BasicPiece instantiation
        king = board.add_piece(BasicPiece('W', 'king', (6, 2))) # A white king on G3

        queen.update_all_moves(board)
        all_moves = queen.all_moves

        self.assertTrue(len(all_moves) == 15)
        self.assertIn(((0, 6), "N"), all_moves)
        self.assertIn(((1, 6), "N"), all_moves)
        self.assertIn(((2, 6), "N"), all_moves)
        self.assertIn(((3, 6), "N"), all_moves)
        self.assertIn(((4, 6), "N"), all_moves)
        self.assertIn(((5, 6), "N"), all_moves)
        self.assertIn(((7, 6), "N"), all_moves)

        self.assertIn(((5, 7), "N"), all_moves)
        self.assertIn(((7, 5), "N"), all_moves)

        self.assertIn(((4, 4), "C"), all_moves)
        self.assertIn(((5, 5), "N"), all_moves)
        self.assertIn(((7, 7), "N"), all_moves)

        self.assertIn(((6, 7), "N"), all_moves)
        self.assertIn(((6, 5), "N"), all_moves)
        self.assertIn(((6, 4), "C"), all_moves)


        self.assertFalse(pawn_1.is_pinned)
        self.assertFalse(pawn_2.is_pinned)
        self.assertTrue(pawn_3.is_pinned)
        pinned_squares = pawn_3.pinned_squares
        self.assertEqual(len(pinned_squares), 3)
        self.assertIn((6, 6), pinned_squares)
        self.assertIn((6, 5), pinned_squares)
        self.assertIn((6, 3), pinned_squares)




if __name__ == '__main__':
    unittest.main()
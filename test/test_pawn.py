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


    def test_non_captures_for_white(self):
        """
        Ensure that update_all_moves returns only non-captures
        Checks the white-coloured pawns only
        """

        board = Board()

        # Check available moves from starting square
        first_pawn = board.add_piece(Pawn('W', (1, 1))) # a white pawn on B2
        first_pawn.update_all_moves(board)
        first_pawn_all_moves = first_pawn.all_moves

        self.assertEqual(len(first_pawn_all_moves), 2)
        self.assertIn(((1, 2), "N"), first_pawn_all_moves)
        self.assertIn(((1, 3), "N"), first_pawn_all_moves)


        # Check available moves from other square
        second_pawn = board.add_piece(Pawn('W', (1, 3))) # a white pawn on B4
        second_pawn.update_all_moves(board)
        second_pawn_all_moves = second_pawn.all_moves

        self.assertEqual(len(second_pawn_all_moves), 1)
        self.assertIn(((1, 4), "N"), second_pawn_all_moves)

        # Check that the first pawn's moves are now different
        first_pawn.update_all_moves(board)
        first_pawn_all_moves = first_pawn.all_moves

        self.assertEqual(len(first_pawn_all_moves), 1)
        self.assertIn(((1, 2), "N"), first_pawn_all_moves)


        # Check available moves from other square
        third_pawn = board.add_piece(Pawn('W', (2, 5))) # a white pawn on C6
        third_pawn.update_all_moves(board)
        third_pawn_all_moves = third_pawn.all_moves

        self.assertEqual(len(third_pawn_all_moves), 1)
        self.assertIn(((2, 6), "N"), third_pawn_all_moves)

        # Ensure that a new pawn doesn't try to capture its own piece
        fourth = board.add_piece(Pawn('W', (3, 4))) # a white pawn on D5
        fourth.update_all_moves(board)
        fourth_pawn_all_moves = fourth.all_moves

        self.assertEqual(len(fourth_pawn_all_moves), 1)
        self.assertIn(((3, 5), "N"), fourth_pawn_all_moves)



    def test_non_captures_for_black(self):
        """
        Ensure that update_all_moves returns only non-captures
        Checks the black-coloured pawns only
        """

        board = Board()

        # Check available moves from starting square
        first_pawn = board.add_piece(Pawn('B', (5, 6))) # a black pawn on G7
        first_pawn.update_all_moves(board)
        first_pawn_all_moves = first_pawn.all_moves

        self.assertEqual(len(first_pawn_all_moves), 2)
        self.assertIn(((5, 5), "N"), first_pawn_all_moves)
        self.assertIn(((5, 4), "N"), first_pawn_all_moves)


        # Check available moves from other square
        second_pawn = board.add_piece(Pawn('B', (5, 4))) # a black pawn on G5
        second_pawn.update_all_moves(board)
        second_pawn_all_moves = second_pawn.all_moves

        self.assertEqual(len(second_pawn_all_moves), 1)
        self.assertIn(((5, 3), "N"), second_pawn_all_moves)

        # Check that the first pawn's moves are now different
        first_pawn.update_all_moves(board)
        first_pawn_all_moves = first_pawn.all_moves

        self.assertEqual(len(first_pawn_all_moves), 1)
        self.assertIn(((5, 5), "N"), first_pawn_all_moves)


        # Check available moves from other square
        third_pawn = board.add_piece(Pawn('B', (4, 2))) # a black pawn on E3
        third_pawn.update_all_moves(board)
        third_pawn_all_moves = third_pawn.all_moves

        self.assertEqual(len(third_pawn_all_moves), 1)
        self.assertIn(((4, 1), "N"), third_pawn_all_moves)

        # Ensure that a new pawn doesn't try to capture its own piece
        fourth = board.add_piece(Pawn('B', (3, 3))) # a black pawn on D4
        fourth.update_all_moves(board)
        fourth_pawn_all_moves = fourth.all_moves

        self.assertEqual(len(fourth_pawn_all_moves), 1)
        self.assertIn(((3, 2), "N"), fourth_pawn_all_moves)


    def test_captures(self):
        """
        Ensure that update_all_moves returns captures and non-captures
        Checks the both colours of pawns
        """

        board = Board()

        # Check available moves from starting square
        first_white_pawn = board.add_piece(Pawn('W', (1, 1))) # a white pawn on B2
        first_black_pawn = board.add_piece(Pawn('B', (2, 2))) # a black pawn on C3
        first_white_pawn.update_all_moves(board)
        first_black_pawn.update_all_moves(board)
        first_white_pawn_all_moves = first_white_pawn.all_moves
        first_black_pawn_all_moves = first_black_pawn.all_moves

        self.assertEqual(len(first_white_pawn_all_moves), 3)
        self.assertIn(((1, 2), "N"), first_white_pawn_all_moves)
        self.assertIn(((1, 3), "N"), first_white_pawn_all_moves)
        self.assertIn(((2, 2), "C"), first_white_pawn_all_moves)

        self.assertEqual(len(first_black_pawn_all_moves), 2)
        self.assertIn(((2, 1), "N"), first_black_pawn_all_moves)
        self.assertIn(((1, 1), "C"), first_black_pawn_all_moves)

        # Check en-passant for white
        second_white_pawn = board.add_piece(Pawn('W', (1, 4))) # a white pawn on B5
        second_black_pawn = board.add_piece(Pawn('B', (2, 6))) # a black pawn on C7
        second_black_pawn.move_piece((2, 4)) # move the pawn to C5
        board.add_move_to_history((second_black_pawn, (2, 6), (2, 4), 'N'))

        second_white_pawn.update_all_moves(board)
        second_white_pawn_all_moves = second_white_pawn.all_moves
        self.assertEqual(len(second_white_pawn_all_moves), 2)
        self.assertIn(((1, 5), "N"), second_white_pawn_all_moves)
        self.assertIn(((2, 5), "E"), second_white_pawn_all_moves)


        # Check en-passant for black
        third_white_pawn = board.add_piece(Pawn('W', (5, 1))) # a white pawn on F2
        third_black_pawn = board.add_piece(Pawn('B', (6, 3))) # a black pawn on G4
        third_white_pawn.move_piece((5, 3))
        board.add_move_to_history((third_white_pawn, (5, 1), (5, 3), 'N'))

        third_black_pawn.update_all_moves(board)
        third_black_pawn_all_moves = third_black_pawn.all_moves
        self.assertEqual(len(third_black_pawn_all_moves), 2)
        self.assertIn(((6, 2), "N"), third_black_pawn_all_moves)
        self.assertIn(((5, 2), "E"), third_black_pawn_all_moves)













if __name__ == '__main__':
    unittest.main()
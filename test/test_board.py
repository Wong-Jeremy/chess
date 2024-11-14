import unittest
from src.board import Board
from src.piece import BasicPiece

class TestBoard(unittest.TestCase):
    """
    The Pawn class. Contains all the functionality for a pawn on a chess board
    """

    def test_is_valid_square(self):
        """
        Ensure that the static class method is_valid_square works as expected
        """
        for file in range(8):
            for rank in range(8):
                with self.subTest(i=file*8 + rank):
                    self.assertEqual(Board.is_valid_square((file, rank)), True)

        self.assertEqual(Board.is_valid_square((-1, 0)), False)
        self.assertEqual(Board.is_valid_square((0, -1)), False)
        self.assertEqual(Board.is_valid_square((9, 0)), False)
        self.assertEqual(Board.is_valid_square((0, 9)), False)

    def test_basic_instantiation(self):
        """
        Ensure that piece is created and fields are instantiated correctly
        """

        board = Board()
        for file in range(8):
            for rank in range(8):
                with self.subTest(i=file*8 + rank):
                    self.assertIsNone(board.board[rank][file])


    def test_adding_pieces(self):
        """
        Ensure pieces get added and are accessible
        """
        board = Board()
        # create a white piece on A1
        piece_1 = board.add_piece(BasicPiece("W", "NA", (0, 0)))
        # create a black piece on H8
        piece_2 = board.add_piece(BasicPiece("B", "NA", (7, 7)))

        self.assertEqual(piece_1, board.get_piece_from_position((0, 0)))
        self.assertEqual(piece_2, board.get_piece_from_position((7, 7)))

    def test_removing_pieces(self):
        """
        Ensure pieces get removed from position and removed from active pieces
        """
        board = Board()
        # create a white piece on A1
        pos1 = (0, 0)
        piece_1 = BasicPiece("W", "NA", pos1)
        board.add_piece(piece_1)
        # create a black piece on H8
        pos2 = (7, 7)
        piece_2 = BasicPiece("B", "NA", pos2)
        board.add_piece(piece_2)

        self.assertIn(piece_1, board.active_white_pieces)
        self.assertIn(piece_2, board.active_black_pieces)

        self.assertEqual(piece_1.is_active_piece, True)
        self.assertEqual(piece_2.is_active_piece, True)

        board.remove_piece_by_square(pos1)
        board.remove_piece_by_square(pos2)

        self.assertNotIn(piece_1, board.active_white_pieces)
        self.assertNotIn(piece_2, board.active_black_pieces)

        self.assertEqual(piece_1.is_active_piece, False)
        self.assertEqual(piece_2.is_active_piece, False)

        self.assertIn(piece_1, board.inactive_pieces)
        self.assertIn(piece_2, board.inactive_pieces)

    def test_move_history(self):
        """
        Ensure that the moves get added to the history
        """

        board = Board()
        piece = BasicPiece("W", 'NA', (0,0))

        move_1 = (piece, (0, 0), (1, 1), 'N')
        board.add_move_to_history(move_1)

        move_2 = (piece, (0, 0), (2, 3), 'C')
        board.add_move_to_history(move_2)

        last_move = board.get_last_move()
        self.assertTupleEqual(move_2, last_move)
        move_history = board.get_move_history()
        self.assertTupleEqual(move_1, move_history[0])
        self.assertTupleEqual(move_2, move_history[1])



if __name__ == '__main__':
    unittest.main()

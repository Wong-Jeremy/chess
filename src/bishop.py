""" This module implements the Bishop piece """

from src.piece import BasicPiece

class Bishop(BasicPiece):
    """
    The Bishop class. Contains all the functionality for a bishop on a chess board.
    """

    def __init__(self, colour, pos):
        BasicPiece.__init__(self, colour, 'bishop', pos)
        self.xray_squares = []

    def update_all_moves(self, board):
        self.all_moves = []
        self.xray_squares = []
        self.squares_defended = []

        # Check upper left
        self.check_direction(-1,  1, board)
        # Check upper right
        self.check_direction( 1,  1, board)
        # Check lower left
        self.check_direction(-1, -1, board)
        # Check lower right
        self.check_direction( 1, -1, board)




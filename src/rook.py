""" This module implements the Rook piece """

from src.board import Board
from src.piece import BasicPiece

class Rook(BasicPiece):
    """
    The Rook class. Contains all the functionality for a rook on a chess board.
    """

    def __init__(self, colour, pos):
        BasicPiece.__init__(self, colour, 'rook', pos)
        self.xray_squares = []

    def update_all_moves(self, board):
        self.all_moves = []
        self.xray_squares = []
        self.squares_defended = []

        # Check up
        self.check_direction( 0,  1, board)
        # Check down
        self.check_direction( 0, -1, board)
        # Check right
        self.check_direction( 1,  0, board)
        # Check left
        self.check_direction(-1,  0, board)

""" This module implements the Knight piece """

from src.board import Board
from src.piece import BasicPiece

class Knight(BasicPiece):
    """
    The Knight class. Contains all the functionality for a knight on a chess board.
    """

    def __init__(self, colour, pos):
        BasicPiece.__init__(self, colour, 'knight', pos)

    def update_all_moves(self, board):
        self.all_moves = []
        self.squares_defended = []

        # Relative directions given clockwise from the 12-o-clock position
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        for (rank, file) in directions:
            target_square = (self.pos[0] + rank, self.pos[1] + file)
            if not Board.is_valid_square(target_square):
                continue

            target_square_piece = board.get_piece_from_position(target_square)
            if not target_square_piece:
                self.all_moves.append((target_square, "N"))
                self.squares_defended.append(target_square)
            elif target_square_piece:
                if target_square_piece.get_colour() == self.get_colour():
                    continue
                elif target_square_piece.get_colour() != self.get_colour():
                    self.all_moves.append((target_square, "C"))
                    self.squares_defended.append(target_square)


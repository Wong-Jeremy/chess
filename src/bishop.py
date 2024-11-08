""" This module implements the Bishop piece """

from src.board import Board
from src.piece import BasicPiece

class Bishop(BasicPiece):
    """
    The Bishop class. Contains all the functionality for a bishop on a chess board.
    """

    def __init__(self, colour, pos):
        BasicPiece.__init__(self, colour, 'bishop', pos)
        self.xray_squares = []

    def get_all_moves(self, board):
        self.all_moves = []
        self.xray_squares = []

        def check_direction(file, rank):
            is_xray = False
            # For backtracking x_ray squares
            num_moves = 0
            
            check_square = (self.pos[0] + file, self.pos[1] + rank)
            while Board.is_valid_square(check_square):
                piece_at_square = board.get_piece_from_position(check_square)
                if not board.get_piece_from_position(check_square):
                    self.all_moves.append(check_square, 'N')
                    num_moves += 1
                elif piece_at_square.get_colour() == self.get_colour():
                    break
                elif piece_at_square.get_colour() != self.get_colour():
                    self.all_moves.append(check_square, 'C')
                    num_moves += 1
                    is_xray = True
                    break
            
            # Exists to speed up pinned piece checks
            if is_xray:
                potential_pinned_squares = []
                reverse_pinned_squares = [l[0] for l in self.all_moves[-num_moves:-1]]
                check_square = (check_square[0] + file, check_square[1] + rank)
                while Board.is_valid_square(check_square):
                    piece_at_square = board.get_piece_from_position(check_square)
                    if not piece_at_square:
                        potential_pinned_squares.append(check_square)
                    elif piece_at_square.get_colour() == self.get_colour():
                        break
                    elif piece_at_square.get_colour() != self.get_colour():
                        if piece_at_square.get_piece_type() == 'king':
                            piece_at_square.is_pinned = True
                            potential_pinned_squares.extend(reverse_pinned_squares)
                            piece_at_square.pinned_squares = potential_pinned_squares[:]
                        break

                        
        # Check upper left
        check_direction(-1,  1)
        # Check upper right
        check_direction( 1,  1)
        # Check lower left
        check_direction(-1, -1)
        # Check lower right
        check_direction( 1, -1)
        
        


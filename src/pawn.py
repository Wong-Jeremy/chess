""" This module implements the Pawn piece """

from src.board import Board
from src.piece import BasicPiece


class Pawn(BasicPiece):
    """
    The Pawn class. Contains all the functionality for a pawn on a chess board.
    """
    
    def __init__(self, colour, pos):
        BasicPiece.__init__(self, colour, 'pawn', pos)
        """
        This is the only piece that gets instantiated with the previous square being the starting square.
        It allows for one less variable when checking if a two square move is valid
        """
        self.previous_square = pos
    
    def get_all_moves(self, board): 
        self.all_moves = []
        self.squares_defended = []
        

        # TODO
        # Refactor to remove repetition. Can use a *-1 to denote movement for black pieces
        
        # Consider a white pawn
        if self.get_colour() == 'W':
            left_attacking_square = (self.pos[0] - 1, self.pos[1] + 1)
            if Board.is_valid_square(left_attacking_square):
                self.squares_defended.append(left_attacking_square)
                if (board.get_piece_from_position(left_attacking_square) and board.get_piece_from_position(left_attacking_square).get_colour() == 'B'):
                    self.all_moves.append((left_attacking_square, 'C'))
            right_attacking_square = (self.pos[0] + 1, self.pos[1] + 1)
            if Board.is_valid_square(right_attacking_square):
                self.squares_defended.append(right_attacking_square)
                if board.get_piece_from_position(right_attacking_square) and board.get_piece_from_position(right_attacking_square).get_colour() == 'B':
                    self.all_moves.append((right_attacking_square, 'C'))
        
            # This will always be a valid square since promotion would have occurred otherwise
            # The only scenario would be if the board is built incorrectly
            # Avoid this by preventing pawns from being placed on the first and last rank
            square_ahead = (self.pos[0], self.pos[1] + 1)

            if not board.get_piece_from_position(square_ahead):
                self.all_moves.append((square_ahead, 'N'))

                # Check for the two square move
                two_squares_ahead = (self.pos[0], self.pos[1] + 2)
                
                # check that the two square move is empty AND that the pawn has not yet moved
                # ie. it is on the second rank
                if not board.get_piece_from_position(square_ahead) and self.previous_square[1] == 2:
                    self.all_moves.append((two_squares_ahead, 'N'))

            # TODO
            # Code for en-passant here
            # Check that self is on the correct file
            if self.pos[1] == 4:
                previous_board_move = board.get_last_move()
                piece = previous_board_move[0]
                piece_old_pos = previous_board_move[1]
                piece_new_pos = previous_board_move[2]
                # Check that the previous move was a pawn move
                # and that it is on one of the adjacent files
                if piece.get_piece_type() == 'Pawn' and (piece_new_pos[0] == self.pos[0] - 1 or piece_new_pos[0] == self.pos[0] + 1):
                    # CHeck that the move was a two square move
                    if piece_new_pos[1] == 4 and piece_old_pos[1] == 6:
                        self.all_moves.append(((piece_new_pos[0], 5), 'E'))





        # Consider a black pawn
        if self.get_colour() == 'W':
            left_attacking_square = (self.pos[0] - 1, self.pos[1] - 1)
            if Board.is_valid_square(left_attacking_square):
                self.squares_defended.append(left_attacking_square)
                if (board.get_piece_from_position(left_attacking_square) and board.get_piece_from_position(left_attacking_square).get_colour() == 'W'):
                    self.all_moves.append((left_attacking_square, 'C'))
            right_attacking_square = (self.pos[0] + 1, self.pos[1] - 1)
            if Board.is_valid_square(right_attacking_square):
                self.squares_defended.append(right_attacking_square)
                if board.get_piece_from_position(right_attacking_square) and board.get_piece_from_position(right_attacking_square).get_colour() == 'W':
                    self.all_moves.append((right_attacking_square, 'C'))
        
            # This will always be a valid square since promotion would have occurred otherwise
            # The only scenario would be if the board is built incorrectly
            # Avoid this by preventing pawns from being placed on the first and last rank
            square_ahead = (self.pos[0], self.pos[1] - 1)

            if not board.get_piece_from_position(square_ahead):
                self.all_moves.append((square_ahead, 'N'))

                # Check for the two square move
                two_squares_ahead = (self.pos[0], self.pos[1] - 2)
                if not board.get_piece_from_position(square_ahead) and self.previous_square[1] == 6:
                    self.all_moves.append((two_squares_ahead, 'N'))

            # TODO
            # Code for en-passant here
            if self.pos[1] == 3:
                previous_board_move = board.get_last_move()
                piece = previous_board_move[0]
                piece_old_pos = previous_board_move[1]
                piece_new_pos = previous_board_move[2]
                # Check that the previous move was a pawn move
                # and that it is on one of the adjacent files
                if piece.get_piece_type() == 'Pawn' and (piece_new_pos[0] == self.pos[0] - 1 or piece_new_pos[0] == self.pos[0] + 1):
                    # CHeck that the move was a two square move
                    if piece_new_pos[1] == 3 and piece_old_pos[1] == 1:
                        self.all_moves.append(((piece_new_pos[0], 2), 'E'))
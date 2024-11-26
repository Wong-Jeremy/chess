""" This module implements a superclass piece, which defines the field and
methods that most subclass pieces will implement."""

from src.board import Board

class BasicPiece():
    """
    A superclass for which each piece has to subclass. All 'chess' moves are determined in the
    respective subclass. This class contains the necessary fields and logical methods.
    """

    def __init__(self, colour, piece_type, pos):
        # Basic elements
        self.pos = pos
        self.legal_moves = []

        # "Private" fields
        self.__colour = colour
        self.__type = piece_type
        self.__starting_square = pos

        # Other metadata
        self.previous_square = None
        self.all_moves = []
        self.squares_defended = []
        self.is_pinned = False
        self.pinned_squares = []
        self.is_active_piece = True

    def __eq__(self, other):
        """
        Dunder equality method. Relies on starting square 'private' variable
        Position is not used since inactive pieces no longer have a position.
        """
        if isinstance(other, BasicPiece):
            # position alone should be sufficient for equality, but in extra redundancy with this
            # Additionally, this method should not be called too frequently
            return (
                self.get_starting_square() == other.get_starting_square() and
                self.get_colour() == other.get_colour() and
                self.get_piece_type() == other.get_piece_type())
        return False

    def __neq__(self, other):
        """
        Dunder inequality method. Is the equality method with De Morgan's rule applied.
        """
        if isinstance(other, BasicPiece):
            # position alone should be sufficient for equality, but in extra redundancy with this
            # Additionally, this method should not be called too frequently
            return (self.pos != other.pos or self.get_colour() != other.get_colour() or self.get_piece_type() != other.get_piece_type())
        return False

    # For hashing, if necessary in the future, can define a field: starting_square

    def get_colour(self):
        """
        Get the colour of the piece.

        This 'get' method prevents users from accidentally changing the piece color
        in the future.
        """
        return self.__colour

    def get_piece_type(self):
        """
        Get the type of the piece (pawn, bishop, knight, etc...).

        This 'get' method prevents users from accidentally changing the piece color
        in the future.
        """
        return self.__type

    def get_starting_square(self):
        """
        Get the starting square of the piece.

        This get method prevents users from accidentally changing the piece color
        in the future. It is imperative that this field is never changed after instantiation.
        It will break the equality relationship if the field is ever changed.
        """
        return self.__starting_square

    def move_piece(self, new_pos):
        """
        Moves the piece

        Parameters:
        pos (tuple): square on the board in (rank, file) format
        board (Board class): the current board

        Returns:
        None

        """
        self.previous_square = self.pos[:]
        self.pos = new_pos[:]

    def update_all_moves(self, board):
        """
        Get all the possible moves for this piece.
        Not all of these moves will be legal.

        Updates the field `all_moves`.
        """
        raise NotImplementedError("Subclass needs to define this.")


    def get_legal_moves(self, board):
        """
        Determine which of all moves are actually legal moves.
        """
        raise NotImplementedError("Subclass needs to define this.")



    def check_direction(self, file, rank, board):
        """
        Check available moves along a certain direction,
        specified by `file` and `rank` directions.
        Sets the all_moves field in this object.

        Parameters:
        file (int): +1 for increasing file, or -1 for decreasing file

        rank (int): +1 for increasing file, or -1 for decreasing file

        board (object): current board state

        Returns:
        None

        """
        is_xray = False
        potential_pinned_piece = None
        # For backtracking x_ray squares
        num_moves = 0

        check_square = (self.pos[0] + file, self.pos[1] + rank)
        while Board.is_valid_square(check_square):
            self.squares_defended.append(check_square)
            piece_at_square = board.get_piece_from_position(check_square)
            if not board.get_piece_from_position(check_square):
                self.all_moves.append((check_square, 'N'))
                num_moves += 1
                check_square = (check_square[0] + file, check_square[1] + rank)
            elif piece_at_square.get_colour() == self.get_colour():
                break
            elif piece_at_square.get_colour() != self.get_colour():
                self.all_moves.append((check_square, 'C'))
                num_moves += 1
                potential_pinned_piece = piece_at_square
                is_xray = True
                break

        # Exists to speed up pinned piece checks
        if is_xray:
            potential_pinned_squares = []
            reverse_pinned_squares = [l[0] for l in self.all_moves[-num_moves:-1]]
            reverse_pinned_squares.append(self.pos)
            check_square = (check_square[0] + file, check_square[1] + rank)
            while Board.is_valid_square(check_square):
                piece_at_square = board.get_piece_from_position(check_square)
                if not piece_at_square:
                    potential_pinned_squares.append(check_square)
                elif piece_at_square.get_colour() == self.get_colour():
                    break
                elif piece_at_square.get_colour() != self.get_colour():
                    if piece_at_square.get_piece_type() == 'king':
                        potential_pinned_piece.is_pinned = True
                        potential_pinned_squares.extend(reverse_pinned_squares)
                        potential_pinned_piece.pinned_squares = potential_pinned_squares[:]
                    break
                check_square = (check_square[0] + file, check_square[1] + rank)





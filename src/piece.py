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
        pos (tuple): pos (tuple): square on the board in (rank, file) format
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







""" This module controls the board, importing pieces for the game of chess. """

MIN_INDEX = 0
MAX_INDEX = 7

class Board():
    def __init__(self):
        self.board = [
            [None, None, None, None, None, None, None, None]
            for i in range(MAX_INDEX + 1)]
        self.active_white_pieces = []
        self.active_black_pieces = []
        self.inactive_pieces = []
        self.white_in_check = False
        self.black_in_check = False
        self.move_history = []
        self.colour_to_move = 'W'

    @staticmethod
    def is_valid_square(pos):
        """
        Tests whether a given position is a valid square on the board.

        Parameters:
        pos (tuple): square on the board in (rank, file) format

        Returns:
        bool: True if the square is valid, False otherwise

        """
        if (pos[1] >= MIN_INDEX and pos[1] <= MAX_INDEX
            and pos[0] >= MIN_INDEX and pos[0] <= MAX_INDEX):
            return True
        return False

    def move_piece(self, move):
        """
        Makes the move on the board

        Parameters:
        move (tuple of (piece, prev_square, new_square, move_type, ...)): the move to make

        Returns:
        None

        """
        # TODO: implement this


    def get_last_move(self):
        """
        Returns the previous move played. Returns None if there have been no moves yet

        Parameters:
        None

        Returns:
        last_move (tuple): the last move played, in the format (piece, prev_square, new_square, details, )
            - where details is a capture, non-capture, en-passant, castle

        """
        if len(self.move_history) > 0:
            return self.move_history[-1]
        return None

    def add_move_to_history(self, move):
        """
        Adds a move to the move history

        Parameters:
        move (tuple of (piece, prev_square, new_square, move_type, ...)): the move to add

        Returns:
        None

        """

        self.move_history.append(move)
        return None


    def get_move_history(self):
        """
        Returns a copy of the entire move history

        Parameters:
        None

        Returns:
        move_history (list): complete move history as a list

        """
        return self.move_history[:]

    def get_piece_from_position(self, pos):
        """
        Returns the piece at a given position (square) on the board

        Parameters:
        pos (tuple): pos (tuple): square on the board in (rank, file) format

        Returns:
        piece (subclass of BasicPiece): the piece at the given position. None if it is empty.

        """
        return self.board[pos[1]][pos[0]]

    def add_piece(self, piece):
        """
        Adds a piece to the board

        Parameters:
        piece (subclass of BasicPiece): the piece to be added to the board

        Returns:
        piece (subclass of BasicPiece): the piece that was added

        """
        self.board[piece.pos[1]][piece.pos[0]] = piece
        piece.is_active_piece = True
        if piece.get_colour() == 'W':
            self.active_white_pieces.append(piece)
        if piece.get_colour() == 'B':
            self.active_black_pieces.append(piece)

        return piece

    def remove_piece_by_square(self, pos):
        """
        Remove a piece at the position (square) on the board, if any.
        Also sets that piece to inactive.

        Parameters:
        pos (tuple): pos (tuple): square on the board in (rank, file) format

        Returns:
        piece (subclass of BasicPiece): the removed piece, with fields updated

        """
        piece_to_remove = self.board[pos[1]][pos[0]]
        if piece_to_remove.get_colour() == "W":
            self.active_white_pieces[:] = list(filter(
                lambda item: item != piece_to_remove, self.active_white_pieces))
        if piece_to_remove.get_colour() == "B":
            self.active_black_pieces[:] = list(filter(
                lambda item: item != piece_to_remove, self.active_black_pieces))

        self.board[pos[1]][pos[0]] = None
        self.inactive_pieces.append(piece_to_remove)
        piece_to_remove.is_active_piece = False




    def refresh_all_active_pieces(self):
        """
        Updates all the active peices on the board.
        Reinstantiates the active_black and active_white_pieces by iterating
        over all squares on the board.

        This function shouldn't be called except for debugging purposes.
        Proper coding should keep track of all of the pieces.

        Parameters:
        pos (tuple): pos (tuple): square on the board in (rank, file) format

        Returns:
        piece (subclass of BasicPiece): the piece at the given position. None if it is empty.

        """
        del self.active_white_pieces
        self.active_white_pieces = []
        del self.active_black_pieces
        self.active_black_pieces = []

        for rank in range(MAX_INDEX):
            for file in range(MAX_INDEX):
                piece = self.board[file][rank]
                if piece:
                    if piece.get_colour() == "W":
                        self.active_white_pieces.append(self.board[file][rank])
                    if piece.get_colour() == "B":
                        self.active_black_pieces.append(self.board[file][rank])


    def remove_all_pieces(self):
        """
        Removes all pieces on the board. Sets them to inactive pieces

        This function shouldn't be called except for debugging purposes.
        Proper coding should keep track of all of the pieces.

        Parameters:
        None

        Returns:
        None

        """

        for rank in range(MAX_INDEX):
            for file in range(MAX_INDEX):
                piece = self.board[file][rank]
                if piece:
                    if piece.get_colour() == "W":
                        self.active_white_pieces.append(self.board[file][rank])
                    if piece.get_colour() == "B":
                        self.active_black_pieces.append(self.board[file][rank])

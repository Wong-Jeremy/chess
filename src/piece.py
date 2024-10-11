

class BasicPiece():

    def __init__(self, colour, piece, pos):
        self.colour = colour
        self.piece = piece
        self.pos = pos

    def move_piece(self, pos):
        self.pos = pos

    def get_legal_moves(self, board):
        raise NotImplementedError("Subclass needs to define this.") 
``
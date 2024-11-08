# chess
Building a chess engine from scratch. Not following any guides, just building it from intuition.


## Representation
Standard 8x8 chess board. 

### Moves
All moves follow typical chess notation. In code, they are represented by a tuple containing
1. A tuple of the rank and file that the piece will be moving to
2. A string of "C" or "N" (or rarely "E", for en-passant), where "C" denotes capture and "N" denotes a non-capturing move. This was originally implemented to account for pawns' behaviour, but it isn't actually necessary because the final destination will denote if it's a capture or a move anyway

For recording move history, the typical chess notation will be used. This will be done using a tuple consisting of:
1. the piece
2. the square of the piece before the move
3. the square of the piece after the move
4. a string denoting whether it is a capture ('C'), non-capture ('N'), en-passant ('E'), or castle ('O')
5. an additional marker for determining if two of the same pieces can make the same move


### Piece Class
Pieces should be identified during the game by the square they are on. However, for equality purposes, pieces will be defined by their starting square and their colour. 

Fields: 
1. Colour: Str, either 'W' or 'B'
2. Position: should be a tuple representing chess notation. ie. (0, 4): A5, (7, 7): H8. 
3. Type of piece
4. Squares attacking: array of squares it can move to
5. Legal moves: not the same as above in the event of a pin
6. x-ray squares
Methods:
1. Move piece.
2. Get All Attacking Squares
3. Get Legal Moves
4. 

### Board class
Representation: board array is 0-indexed. list of lists. (0, 0) would be A1. (2, 5) would be C6, etc. 

Fields in it: 
1. board_state matrix. 8x8. Elements either None or Piece class
2. piece_list array variable
3. black_king_pos and white_king_pos variables. For easier legal moves calculator
4. colour_in_check: boolean for if a colour is in check. One for white and one for black.
5. boolean variables for if castling is still allowed
6. colour_to_move: to keep track of whose turn it is
7. move_history: a list of tuples (defined above)
Methods in it
1. Move piece. 
2. Update all moves in same row and diagonals after piece move


# chess_project
Interactive chess game using Python, Pygame, Numpy. AI to play against.


Three code files: chess_piece.py, chess_init.py, chessgame.py
The other files are images.

chess_piece.py creates a class called piece, which describes all the possible moves every chess piece can make (except from castling) within the context of an 8 by 8 numpy array. Instances of this class are created, and these objects are all the white and black chess pieces.

chess_init.py handles the graphics for the game using the pygame module, and controls the order in which the game is played in the game's while loop. It also handles moves such as castling, describes what happens when a piece is taken, and can tell when a player is in checkmate or if there is a stalemate.

chessgame.py handles the AI. The function program_white describes the logic behind the chess AI for both white and black players. There is the option to have the AI to play completely random (but legal) moves, or for it to 'try' to win through this logic.

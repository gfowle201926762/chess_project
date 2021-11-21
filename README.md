# chess_project
An interactive chess game which uses Python3.6 and the modules Pygame and Numpy. Two humans can play against each other, or you can play against an AI, or you can see what happens when the AI plays itself.


Three code files: chess_piece.py, chess_init.py, chessgame.py. Run chess_init.py to play.
The other files are images.

chess_piece.py creates a class called piece, which describes all the possible moves every chess piece can make (except from castling and en passant) within the context of an 8 by 8 numpy array. Instances of this class are created, and these objects are all the white and black chess pieces.

chess_init.py handles the graphics for the game using the pygame module, and controls the order in which the game is played in the game's while loop. It also handles moves such as castling, describes what happens when a piece is taken, and can tell when a player is in checkmate or if there is a stalemate. If you want to run the game, run this file using python3.6.

chessgame.py handles the AI. The function program_white describes the logic behind the chess AI for both white and black players. There is the option to have the AI to play completely random (but legal) moves, or for it to 'try' to win through this logic.

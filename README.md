# chess_project

## Overview
Run chess_init.py to play. An interactive chess game which uses Python and the modules Pygame and Numpy. Two humans can play against each other, or you can play against an AI, or you can see what happens when the AI plays itself.

## Libraries used
- Pygame
- Numpy

## Description
Three code files: chess_piece.py, chess_init.py, chessgame.py. Run chess_init.py to play.
The other files are images.

chess_piece.py creates a class called piece, which describes all the possible moves every chess piece can make (except from castling and en passant) within the context of an 8 by 8 numpy array. Instances of this class are created, and these objects are all the white and black chess pieces.

chess_init.py handles the graphics for the game using the pygame module, and controls the order in which the game is played in the game's while loop. It also handles moves such as castling, describes what happens when a piece is taken, and can tell when a player is in checkmate or if there is a stalemate. If you want to run the game, run this file using python3.6.

chessgame.py handles the AI. The function program_white describes the logic behind the chess AI for both white and black players. There is the option to have the AI to play completely random (but legal) moves, or for it to 'try' to win through this logic.

## The game
The start screen: Black and white can be played by a human, or an AI which plays random moves, or an AI which plays intelligent (relatively speaking) moves.
![alt text](https://github.com/gfowle201926762/chess_project/blob/main/Screenshot%202022-01-03%20at%2012.32.21.png?raw=true)

Intuitive moves: Click on a piece to see where you can move it. If the opponent is the AI, it will move automatically once you have played. The last move played by your opponent will show on the screen with the change of tile colours.
![alt text](https://github.com/gfowle201926762/chess_project/blob/main/Screenshot%202022-01-03%20at%2012.33.23.png?raw=true)

Checkmate: Once a player is in checkmate, the game will end.
![alt text](https://github.com/gfowle201926762/chess_project/blob/main/Screenshot%202022-01-03%20at%2012.35.43.png?raw=true)


## Challenges
This project had several challenges, especially considering it was the first large project I have completed. Correctly configuring pygame's while loop with such complex move sequences was an initial difficulty. Building the logic for the AI was particularly time consuming, especially when factoring in chess positions which would only become relevant several moves down the line. Chess has a large branching factor which quickly overloads computation time, therefore I had to find ways to artificially choose which future moves should factor in to its final decision.

## What I learnt
Given this was my first large project, I learnt a lot about basic and intermediate programming concepts with Python such as classes, loops, accessing data from lists, and finding ways to optimise computing time. Beyond the Python language itself, this project taught me how to convert game positions into computer-readable format, and to find proxies for determining which move is 'better' or 'worse' which the programme can then use as a heuristic.

## Future features
I would like to build a similar programme for the Go board game. Chess has distinct tells which make it easier to decide whether a move is good or bad, such as taking an opponent's piece which has a high value. On the other hand, Go has no such obvious tells which help decide the next move. I am curious as to what heuristics a programme could potentially use, and I would enjoy the challenge of implementing them.

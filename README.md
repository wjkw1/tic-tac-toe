# Tic Tac Toe
Write a simple tic tac toe game in python. The game can be text based, e.g. the users play it via the command line/terminal. The players should take turns to move and can see the current board position at each step. It should let them know when they win, lose or draw. 

## Bonus: 
The user plays against the computer -  write a programme that makes a move after the player makes a move. This is very much a bonus step - in our internal validation of this exercise we didn’t complete this bonus step.


## Rules:
You have 4 hours max. You don't need to use all 4 hours.

As far as use of Google or use of the internet, you are on the honour code. This is a programming exercise so you are welcome to search for programming things like "how to get user input from the command line in python" but you are not allowed to search for, or use, tic tac toe examples online. We are aware of a few examples online, so it’s best not to even look at them in case your code too closely resembles their approach.

If you don't know how to play tic tac toe,  see https://www.wikihow.com/Play-Tic-Tac-Toe

# Additional Features I'd like to add

With more time I would:

- Add restart functionality so the game can play endlessly
- Add a Player class that uses player names, player token and their number
- Create a game state object for state, rather than use a list
- Add slot class, with row and board classes, so we can make it generic how many rows we add for our board
- Control the game state from within the Game class
- optimise the win condition loop, to only check current token added

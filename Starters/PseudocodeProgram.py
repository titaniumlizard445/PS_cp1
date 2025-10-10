#PS 1st taking the pseudocode from the board and turning it into a program

import random
board = ["","","","","","","","",""]

if board[1] == "o" and board[4] == "o" and board[7] == "o":
    print("You win")
elif board[2] == "o" and board[5] == "o" and board[8] == "o":
    print("You win")
elif board[3] == "o" and board[6] == "o" and board[9] == "o":
    print("You win")


if board[1] == "x" and board[2] == "x" and board[3] == "x":
    print("You win")
elif board[4] == "x" and board[5] == "x" and board[6] == "x":
    print("You win")
elif board[7] == "x" and board[8] == "x" and board[9] == "x":
    print("You win")
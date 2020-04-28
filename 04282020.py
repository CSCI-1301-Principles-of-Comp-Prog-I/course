#!/usr/local/bin/python3.8

import list_lib

# Tick-Tac-Toe : Using functions.

# Global constants, not able to be updated.
blank_sym = '*'
player_syms = ['O', 'X']

# Returns True if board is solved, and false otherwise.
def isSolved(board):
    _solved = [blank_sym for row in board for (r,c,s) in row if s == blank_sym]
    return _solved == []

# Returns True if player_sym is the winner, and false otherwise.
def checkWinner(board, player_sym):
    board_bool = [[(r,c,s == player_sym) for (r,c,s) in row] for row in board]
    row_bool   = [list_lib.all ([b for (r,c,b) in row]) for row in board_bool]
    row_win    = list_lib.any (row_bool)

    colums = [[b for row in board_bool for (r,c,b) in row if c == col] for col in [0,1,2]]
    col_bool = [list_lib.all(colums)]
    col_win = list_lib.any (col_bool)

    main_diag = [b for row in board_bool for (r,c,b) in row if r == c]
    main_diag_win = list_lib.all (main_diag)

    antidiag = [b for row in board_bool for (r,c,b) in row if c == 2 - r]
    antidiag_win = list_lib.all(antidiag)

    return row_win or col_win or main_diag_win or antidiag_win

# Convert the board into a string to be printed to the screen for the
# user.
def board2String(board):
    output = ""

    for row in board:
        output += "|"
        for (_,_,d) in row:
            output += d + "|"
        output += "\n"

    return output

# Updates the player:
def updatePlayer(current_player):
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    return current_player

# Asks the user for their next move:
def getNextMove(current_player):
    row = 0
    col = 0
    correct_input = False

    print("Player "+current_player+"'s move.")    
    while not correct_input:
        row = int(input("Enter the row: "))
        if not (0 <= row <= 3):
            print("Invalid input, please enter a row between 0 and 3.")
            continue
        correct_input = True

    correct_input = False
    while not correct_input:
        col = int(input("Enter the col: "))    
        if not (0 <= col <= 3):
            print("Invalid input, please enter a col between 0 and 3.")
            continue

        correct_input = True

    return (row,col)

# Update the board with a new move:

# board = 
# [
#  [(0, 0, '*'), (0, 1, '*'), (0, 2, '*'), (0, 3, '*')],
#  [(1, 0, '*'), (1, 1, '*'), (1, 2, '*'), (1, 3, '*')],
#  [(2, 0, '*'), (2, 1, '*'), (2, 2, '*'), (2, 3, '*')],
#  [(3, 0, '*'), (3, 1, '*'), (3, 2, '*'), (3, 3, '*')]
# ]
#
# board[0] =
# [(0, 0, '*'), (0, 1, '*'), (0, 2, '*'), (0, 3, '*')]
#
# board[0][0]
# (0, 0, '*')


def updateBoard(board, row, col, current_player):
    board[row][col] = (row,col,current_player)
    return board

# Main loop: offically play a game.
def play():
    board = [[(r,c,blank_sym) for c in range(4)] for r in range(4)]
    current_player = "X"

    while True:                
        print(board2String(board))

        (row,col) = getNextMove(current_player)

        board = updateBoard(board, row, col, current_player)
        
        if isSolved(board): break

        current_player = updatePlayer(current_player)

    print(board2String(board))
    win = checkWinner(board, current_player)
    if win:
        print (current_player+" won!")
    else:
        updatePlayer()
        win = checkWinner(board, current_player)
        if win:
            print (current_player+" won!")
        else:
            print("Error occured")

if __name__ == "__main__":
    play()

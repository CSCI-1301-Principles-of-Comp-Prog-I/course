import list_lib as ll

# Using for-loops and given a blank 10 x 10 board called board.
# Mark every other cell with a X.  Then print the board out in
# for format of a game board.
board = [[(r,c,'-') for c in range(0,10)] for r in range(0,10)]

for row in board:
    new_row = []
    for (r,c,d) in row:        
        if c % 2 == 0:
            new_row = ll.cons((r,c,'X'), new_row)
        else:
            new_row = ll.cons((r,c,d), new_row)

# Redo do this problem using a list comprehension.

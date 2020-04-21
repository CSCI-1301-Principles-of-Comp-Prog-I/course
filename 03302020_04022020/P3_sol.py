import list_lib as ll

# Using for-loops and given a blank 10 x 10 board called board.
# Mark every other cell with a X.  Then print the board out in
# for format of a game board.

board = [[(r,c,'-') for c in range(0,10)] for r in range(0,10)]
new_board = []
for row in board:
    new_row = []
    for (r, c, d) in row:
        if c % 2 == 0:
            new_row = ll.cons((r,c,"X"),new_row)
        else:
            new_row = ll.cons((r,c,d),new_row)
    new_row = ll.reverse(new_row)
    new_board = ll.cons(new_row,new_board)
new_board = ll.reverse(new_board)

output = "  "
row_i = 0
for col_i in range(0,10):
    output = output + " " + str(col_i)
output = output + "\n"

for row in new_board:
    if row_i < 10:
        output = output + " " + str(row_i) + "|"
    else:
        output = output + str(row_i) + "|"
    for (r,c,d) in row:
        output = output + str(d) + "|"
    output = output + "\n"
    row_i = row_i + 1

print(output)

# Redo do this problem using a list comprehension.

new_board2 = [[(r,c,('X' if c % 3 == 0 else d)) for (r,c,d) in row] for row in board]

output = "  "
row_i = 0
for col_i in range(0,10):
    output = output + " " + str(col_i)
output = output + "\n"

for row in new_board2:
    if row_i < 10:
        output = output + " " + str(row_i) + "|"
    else:
        output = output + str(row_i) + "|"
    for (r,c,d) in row:
        output = output + str(d) + "|"
    output = output + "\n"
    row_i = row_i + 1

print(output)

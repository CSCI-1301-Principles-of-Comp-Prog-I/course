import list_lib as ll

# Using for-loops and given a blank 10 x 10 board called board.
# Mark every other cell with a X.  Then print the board out in
# for format of a game board.
board = [[(r,c,'-') for c in range(0,20)] for r in range(0,20)]

new_board = []
for row in board:
    new_row = []
    for (r,c,d) in row:        
        if c % 2 != 0:
            new_row = ll.append(new_row,[(r,c,'X')])
        else:
            new_row = ll.append(new_row, [(r,c,d)])
    new_board = ll.append(new_board, [new_row])

#     0 1 2 3
#  0 |-|-|-|-|
#  1 |-|-|-|-|
#  2 |-|-|-|-|
#  3 |-|-|-|-|

output = ""
# Column index header:
row_size = ll.length(new_board)
output += "   "
for col_index in range(0,row_size):
    output += str(col_index) + " "
output += "\n"

# Rows to string:
for row in new_board:
    (row_index,_,d) = ll.head(row)
    rest_rows = ll.tail(row)
    row_str = "|"+d
    for (r,c,d) in rest_rows:
        cell = "|"+d
        row_str += cell    # output = output + cell
    if row_index < 10:
        row_str = " " + str(row_index) + " " + row_str + "|\n"
    else:
        row_str = str(row_index) + " " + row_str + "|\n"
    output += row_str

print(output)



# Redo do this problem using a list comprehension.

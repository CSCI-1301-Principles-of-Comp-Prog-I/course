import list_lib
import movies

# 0. Given the following operations:
#      - all : takes a list of booleans, and returns true if every
#              element is true, but false otherwise,
#      - any : takes a list of booleans, and returns true if any
#              element is true, and false otherwise.
#    Using the above operations and a list comprehension determine 
#    if every element of a list of integers, called ints, is
#    greater than 4.
ints = list_lib.randint_list(50,0, 1000)

# 1. Given a database of movie titles and release dates, find the
#    list of movies that were released between 1970 and 1980.
#    Print out the first element in this list.
movie_db = movies.get_movies()

# 2. The four-queens problem asks that one place four queens on a
#    4x4-chessboard so that no two queens are attacking each
#    other.  Convert the following board into a list of lists:
#
#     - - - -
#    |*|*|*|Q|
#     - - - -
#    |Q|*|*|*|
#     - - - -
#    |*|*|Q|*|
#     - - - -
#    |*|Q|*|*|
#     - - - -
#
# (1,3)   (2,2)   (3,1)
#
# (2,3)   (3,2)
# (3,3)

# 3. Suppose we are given a board called board.
#    There is a row in board with two queens.

# 4. Do the same, but Determine if two queens are
#    in the same coloumn.

# 5. Ditto, but determine if two queens are in the same
#    diagonal.
board = [[(r,c,'*') for c in range(0,4)] for r in range(0,4)]

main_diag = [(r,c,s) for row in board for (r,c,s) in row if c == r]

diag1 = [(r,c,s) for row in board for (r,c,s) in row if c == r+1]
diag2 = [(r,c,s) for row in board for (r,c,s) in row if c == r+2]
diag3 = [(r,c,s) for row in board for (r,c,s) in row if c == r+3]
diag4 = [(r,c,s) for row in board for (r,c,s) in row if r == c+1]
diag5 = [(r,c,s) for row in board for (r,c,s) in row if r == c+2]
diag6 = [(r,c,s) for row in board for (r,c,s) in row if r == c+3]

main_diag2 = [(r,c,s) for row in board for (r,c,s) in row if c == 3 - r]
diag7 = [(r,c,s) for row in board for (r,c,s) in row if c == 2 - r]
diag8 = [(r,c,s) for row in board for (r,c,s) in row if c == 1 - r]
diag9 = [(0,0)]
diag10 = [(r,c,s) for row in board for (r,c,s) in row if c == 3-(r-1)]

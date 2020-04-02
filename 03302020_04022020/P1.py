import list_lib as ll

# Write the following list comprehension using an explicit for-loop:
#
# squares = [x**2 for x in range(0,43)]
#
# Then write a for-loop to print the list out to the screen in list format.

squares = []
for x in range(0,43):
    squares = ll.cons(x**2,squares)
squares = ll.reverse(squares)

# 1: x = 0, squares = cons(x**2,squares) = cons(0**2,[]) = cons(0,[]) = [0]
# 2: x = 1, squares = cons(x**2,[0]) = cons(1**2,[0]) = cons(1,[0]) = [1,0]
# 3: x = 2, squares = cons(x**2,[1,0]) = cons(2**2,[1,0]) = cons(4,[1,0]) = [4,1,0]

# When trying to output structured data, create the desired output using variables,
# and then output the variable.

output = "["
for i in range(0,ll.length(squares) - 1):
    sq = ll.head(squares)
    squares = ll.tail(squares)
    output = output + str(sq) +", "
sq = ll.head(squares)
output = output + str(sq) + "]"

print(output)

    

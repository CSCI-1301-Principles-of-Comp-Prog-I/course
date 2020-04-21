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

output = "["
for x in range(0,ll.length(squares) - 1):
    next_element = str(ll.head(squares))
    squares = ll.tail(squares)
    output = output + next_element + ", "
last_element = str(ll.head(squares))
output = output + last_element + "]"
print(output)

import list_lib as ll

# Triple each element of the given list of numbers, and output the
# sequence to the screen.
nums = [42, 1, 55, 8, 10]

new_nums = []
for n in nums:
    new_nums = ll.append(new_nums,[n,n,n])
print(new_nums)

import list_lib as ll

# Reverse the given list of numbers using accumilation; the accumilator pattern.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_nums = []  # Accumilator - Accumilates the solution.
for n in nums:
    new_nums = ll.cons(n,new_nums)

print(new_nums)

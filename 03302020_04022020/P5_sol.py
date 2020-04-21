# Reverse the given list of numbers using accumilation.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev = [] # accumilator
for n in nums:
    rev = cons(n,rev)
print(rev)

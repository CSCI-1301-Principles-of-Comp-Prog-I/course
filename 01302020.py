import random

# Suppose we have the following variables with random
# values:
a = random.uniform(0,1000)
b = random.uniform(0,1000)
c = random.uniform(0,1000)

# Solve the following problems:

# Problem 1:
#  Determine which is biggest: a or b.
print ("Problem 1:")

if a > b:
    print ("a is biggest: "+str(a))
elif a == b:
    print ("a and b are equal: "+str(a))
else:
    print ("b is biggest: "+str(b))
print("-------------------------------------------------------------")

# Problem 2:
#  Determine which of a, b, and c is smallest, and which is
#  biggest:
print ("Problem 2:")

print ("a = "+str(a))
print ("b = "+str(b))
print ("c = "+str(c))
if a >= b >= c:
    print("largest: "+str(a))
    print("smallest: "+str(c))
elif a >= c >= b:
    print("largest: "+str(a))
    print("smallest: "+str(b))
elif c >= a >= b:
    print("largest: "+str(c))
    print("smallest: "+str(b))
elif c >= b >= a:
    print("largest: "+str(c))
    print("smallest: "+str(a))
elif b >= c >= a:
    print("largest: "+str(b))
    print("smallest: "+str(a))
else:
    print("largest: "+str(b))
    print("smallest: "+str(c))
print("-------------------------------------------------------------")

# Problem 3: Give values for a, b, and c making the following:
#     (a < b and b != c)
# True, and then give values for which it false.
print ("Problem 3:")
a = 1
b = 2
c = 3

if (a < b and b != c):
    print ("Yes!!")
else:
    print ("No!!")

a = 1
b = 2
c = 2

if (not (a < b and b != c)):
    print ("Yes!!")
else:
    print ("No!!")
    
print("-------------------------------------------------------------")

# Problem 4: Give values for a, b, and c which make the following:
#    (a != b and a == b)
# true and values that make it false.
print ("Problem 4: ")

a = 0
b = 0

if (not (a != b and a == b)):
    print ("Yes!!")
else:
    print ("No!!")

print("-------------------------------------------------------------")

# Problem 5: Give values for a, b, and c which make the following:
#    (a != b or a == b)
# true and values that make it false.

print ("Problem 5: ")

a = 2
b = 2

if (a != b or a == b):
    print ("Yes!!")
else:
    print ("No!!")

a = 2
b = 2

if (not (a != b or a == b)):
    print ("Yes!!")
else:
    print ("No!!")

print("-------------------------------------------------------------")

# Problem 6: Suppose we have the following random variables:
first = random.uniform(0,1000)
second = random.uniform(0,1000)
third = random.uniform(0,1000)

# Using swapping put first, second, third, and forth in order such that
#    first <= second <= third <= forth
# Try to do this in the least number of swaps.

old_first = first
first = second
second = old_first
















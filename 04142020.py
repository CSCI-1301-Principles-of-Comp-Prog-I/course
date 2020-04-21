import list_lib as ll

# Definite iteration : a loop that can be seen to terminate before hand.
# It's a loop we know the number of iterations it will take before hand.
#
# for x in list:
#   block
#
# Indefinite iteration : a loop where we don't know the number of
# iterations before hand.
#
# while b:   (while-loop)
#   block
#
# where b is a boolean.

# An inifite loop.
##while True:
##    print("Hello, give me pizza!")

##while False:
##    print("Hello, give me pizza!")
##
##n = 5
##while n > 0:
##    print("n = "+str(n))
##    print("Hello, pizza, mouth, now!")
##    n -= 1

##n = 5
##while n >= 0:
##    if n % 2 == 0:
##        print("n = "+str(n))
##        print("Hello, pizza, mouth, now!")
##    n -= 1

##n = 25
##while n < 30:
##    print("Hello")
##    n += 1

# Take the sum of nums using a while-loop:
nums = [5,26,42,25,30,50]
nums_len = ll.length(nums)
nums_sum = 0
##while nums_len > 0:
##    n = ll.head(nums)
##    nums = ll.tail(nums)
##    nums_sum += n
##    if nums_sum > 50:
##        break
##    nums_len -= 1
##print("The sum is "+str(nums_sum))

for x in nums:
    print(str(x))
print(nums)

print("-----------------------------")

x = 0
proc_nums = nums
while nums_len > 0:
    x = ll.head(proc_nums)
    proc_nums = ll.tail(proc_nums)
    print(str(x))
    nums_len -= 1
print(nums)

##power_off = false
##while True:
##    ...
##    if power_off:
##        break

##while !stopButtonUp:
##    ...

# Continue : Ends the iteration early (forces loop to return to the condition).

# Break : Ends the loop early.

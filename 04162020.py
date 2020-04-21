import list_lib as ll

nums = [42,35,76,87, 24, 32, 52, 98]
#       0, 1, 2, 3

# print(str(nums[len(nums) - 1]))


##for i in range(len(nums)):
##    print(nums[i])
##
##print("---------------")
##
##i = 0
##while i < len(nums):
##    print(nums[i])
##    i += 1
##

##for i in range(len(nums)):  # Access to elements, with the ability to
##                            # update the array.
##    nums[i] *= 2      # In place replacement.

##for n in nums:   Access to the elements, but without modifiying the array.
##    ...

##print(nums)
##
##nums2 = nums[:]

##nums_doubled = []
##
##for i in nums2:
##    nums_doubled = ll.append(nums_doubled, [ll.head(nums2)])
##    nums2 = ll.tail(nums2)
##
##print(nums_doubled)

# Reversing an array:

# New array version:
numsR = [0 for n in nums]
nums_len = len(nums)
nums_i = nums_len - 1     
numsR_i = 0
c = 0
while nums_i >= 0:
    numsR[numsR_i]= nums[nums_i]
    nums_i -= 1
    numsR_i += 1
    c += 1

print(c)
print(nums)
print(numsR)

# In-place update version:
j = nums_len - 1
c = 0
for i in range(nums_len):    
    if i >= j:
        break
    c += 1
    f = nums[i]
    l = nums[j]
    nums[i] = l
    nums[j] = f
    j -= 1
print(c)
print(nums)

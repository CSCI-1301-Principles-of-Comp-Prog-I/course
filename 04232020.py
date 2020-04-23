import list_lib

# a1 = [1,2,3,4,5]
# a2 = [6,7,8,9,10]
#       0,1,2,3,4                 
# intersperse(a1,a2) = [1,6,2,7,3,8,4,9,5,10]
#                    i  0,1,2,3,4,5,6,7,8,9
#                    a1 0   1   2   3   4
#                    a2   0   1   2   3   4
def intersperse(a1: list, a2: list) -> list :
    if len(a1) != len(a2):
        return []

    # Initialize the array a3 with all 0's:
    a3 = [0] * (len(a1) + len(a2))
    j = 0
    for i in range(len(a3)):
        if i % 2 == 0:
            a3[i] = a1[j]
        else:
            a3[i] = a2[j]
            j += 1
    return a3

# a1 = [1,2,3,4,5]
# a2 = [6,7,8]
#       0,1,2,3,4                 
# intersperse(a1,a2) = [1,6,2,7,3,8]
#                    i  0,1,2,3,4,5,6,7,8,9
#                    a1 0   1   2   3   4
#                    a2   0   1   2   3   4
def intersperse2(a1: list, a2: list) -> list :
    # Initialize the array a3 with all 0's:
    a3 = [0] * (len(a1) + len(a2))
    j = 0
    for i in range(len(a3)):
        if j >= len(a1) or j >= len(a2):
            return a3
        
        if i % 2 == 0:
            a3[i] = a1[j]
        else:
            a3[i] = a2[j]
            j += 1
            
    return a3

print(intersperse2([1,2,3,4,5], [6,7,8]))

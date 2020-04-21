def double(n):
    return 2 * n

def add_three(n):
    return 3 + n

# 3 + (2 * 42)
n = add_three(double(42))
print("0: "+str(n))

# 2 * (3 + 42)
n = double(add_three(42))
print("1: "+str(n))

m = add_three(42)
n = double(m)
print("2: "+str(n))

def array_rev(b):
    a = b[:]
    a_len = len(a)
    j = a_len - 1
    for i in range(a_len):
        if i >= j:
            break
        f = a[i]
        l = a[j]
        a[i] = l
        a[j] = f
        j -= 1
    return a

def array_len(a):
    a_len = 0
    for i in range(len(a)):
        a_len += 1
    return a_len

def star_line(c, output):
    o = output[:]
    for i in range(c):
        o += "*"
    return o

def white_space_padding(c, output):
    o = output[:]
    for i in range(c):
        o += " "
    return o

def header(title, padding_count):
    star_count = len(title) + padding_count * 2 + 2
    output = star_line(star_count, "")
    output += "\n*"
    output = white_space_padding(padding_count,output)
    output += title
    output = white_space_padding(padding_count,output)
    output += "*\n"
    output = star_line(star_count, output)
    return output

##print(header("The Haunting of a Witch", 10))
##print(header("The Haunting of a Witch 2", 20))
##print(header("The Haunting of a Witch 3", 30))




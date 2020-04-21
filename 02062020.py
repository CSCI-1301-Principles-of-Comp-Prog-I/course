import list_lib as ll

# Problem -2. Define a list of the first 6 odd numbers
# using cons.
#
# cons(x,l) - adds x to the front of the list l.
ex_list1 = ll.cons (2, [3,4])
ex_list2 = ll.cons (2, ll.cons(3, ll.cons(4, [])))

odds = ll.cons(1, ll.cons(3, ll.cons (5, ll.cons (7,
                ll.cons (9, ll.cons (11, []))))))


# Problem -1. Given a random list of elements called els, drop
# the first 5, and then take the next 7.
els = ll.randint_list(20,0,100)

print("els = "+str(els))
ds = ll.drop (5, els)
print("ds = "+str(ds))
my_list = ll.take (7, ds)
print("my_list = "+str(my_list))

# Problem 0. Remove all spaces from a string.

# Problem 1. We can convert tempetures from celcius to
# fahrenheit using the following equation:
#
# tf = tc * 1.8 + 32
#
# Given a random list of tempetures in celcius, called temps,
# convert them into fahrenheit.
temps = ll.randfloat_list(15, -150, 150)

print("temps = "+str(temps))
temps_F = [t_C * 1.8 + 32 for t_C in temps]
print("temps_F = "+str(temps_F))


# Problem 2. Given a list of names, called names, in the form
# of ("Last", "First") convert each name into the form
# "First Last".
names = [("Eades",   "Baxter"),
         ("MacLane", "Sanders"),
         ("Lawvere", "William"),
         ("Lambek",  "Joachim")]

# Problem 3. Compute the cartesian product of two random lists
# l1 and l2.
l1 = ll.randint_list(5, 0, 100)
l2 = ll.randint_list(6, 0, 100)

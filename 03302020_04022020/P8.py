import list_lib as ll

# Continue: Given the list of students add one to the each of their
# student ids, and remove Stephanie from the list.

students = [("Jim", "Halport", 10101010),
            ("Michael", "Scott", 2020202),
            ("Pam", "Beesly", 30303030),
            ("Dwight", "Schrute", 40404040),
            ("Stephanie", "Doe", 50505050),
            ("Andy", "Bernard", 606060606)]

new_students = []
length = ll.length(students)

##while length > 0:
##    (first, last, sid) = ll.head(students)
##    students = ll.tail(students)
##    length -= 1
##
##    if first == "Stephanie" and last == "Doe":
##        continue
##    else:
##        sid += 1
##        new_students = ll.cons((first, last, sid),new_students)

first_name = "Pam"
last_name = "Beesly"
found_sid = 0

while length > 0:
    (first, last, sid) = ll.head(students)
    students = ll.tail(students)
    length -= 1

    if first == first_name and last == last_name:
        found_sid = sid
        break # stop looking now!
    print("Still looking..")
print("Found: "+str(found_sid))

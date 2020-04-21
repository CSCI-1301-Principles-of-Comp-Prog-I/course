# Continue: Given the list of students add one to the each of their
# student ids, and remove Stephanie from the list.

students = [("Jim", "Halport", 10101010),
            ("Michael", "Scott", 2020202),
            ("Pam", "Beesly", 30303030),
            ("Dwight", "Schrute", 40404040),
            ("Stephanie", "Doe", 50505050),
            ("Andy", "Bernard", 606060606)]

new_students = []
for (first, last, st_id) in students:
    if first == "Stephanie":
        continue
    new_students += (first, last, st_id + 1)

print(new_students)
        
    


# Break: Find the student "Stephanie" in the given database, store
# their student ID in sid, then terminate the loop and print out their
# student ID.

students = [("Jim", "Halport", 10101010),
            ("Michael", "Scott", 2020202),
            ("Pam", "Beesly", 30303030),
            ("Dwight", "Schrute", 40404040),
            ("Stephanie", "Doe", 50505050),
            ("Andy", "Bernard", 606060606)]

sid = 0
for (first, last, st_id) in students:
    if first == "Stephanie":
        sid = st_id
        break
print(sid)
        
    

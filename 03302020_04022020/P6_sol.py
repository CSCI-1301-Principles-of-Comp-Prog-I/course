# Duplicate every character in the given string.
word = "mathematics"

new_word = ""

for c in word:
    dup = c + c
    new_word += dup
print(new_word)

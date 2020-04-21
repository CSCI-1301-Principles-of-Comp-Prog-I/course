import list_lib as ll

# Treating strings as lists and using for loops.  Factor out of the list
# words every string that begins with the letter 'a' or the letter 't'.
words = ["The", "happy", "student", "did", "their",
         "homework", "and", "ate", "an", "apple"]

result = []
skips = ['T', 't', 'a', 'A']
for word in words:
    first_char = ll.head(word)
    if not (first_char in skips):
        result = ll.cons(word, result)
result = ll.reverse(result)


# Define resolve the problem using a list comprehension, and store your result in
# result2.
result2 = [word for word in words if not (ll.head(word) in skips)]

import list_lib as ll

# Treating strings as lists and using for loops.  Factor out of the list
# words every string that begins with the letter 'a' or 'A' or the letter 't' or 'T'.
words = ["The", "happy", "student", "did", "their",
         "homework", "and", "ate", "an", "apple"]

skips = ['a', 'A', 't', 'T']
found_words = []
for word in words:
    first_char = ll.head(word)
    if not (first_char in skips):
        found_words = ll.cons(word,found_words)
found_words = ll.reverse(found_words)

# Define resolve the problem using a list comprehension, and store your result in
# found_words2.

found_words2 = [word for word in words if not (ll.head(word) in skips)]


# r7e4 - same ignoring case
# Two lines of text. Print whether they are exactly equal, then whether they are equal ignoring case.
# Example: Hello then hello -> prints False then True
a = input()
b = input()
# --- your code below this line ---
print(a == b)
print(a.lower() == b.lower())

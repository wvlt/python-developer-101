# r7e1 - numbered lines
# A whole number n, then n lines of text. Print each line numbered from 1, like:  1. first line
# Use enumerate.
# Example: 2, apple, pear -> prints 1. apple / 2. pear
n = int(input())
lines = [input() for _ in range(n)]  # the n lines as a list (stage 3); you write the loop below
# --- your code below this line ---
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line}")

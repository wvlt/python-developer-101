# r7e1 — numbered lines
# A whole number n, then n lines of text. Print each line numbered from 1, like:  1. first line
# Use enumerate.
# Example: 2, apple, pear -> prints 1. apple / 2. pear
n = int(input())
lines = [input() for _ in range(n)]  # a list of the n lines; lists are stage 3, the loop below is what you write
# --- your code below this line ---

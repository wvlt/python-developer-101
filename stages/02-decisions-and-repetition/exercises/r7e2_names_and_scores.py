# r7e2 — names and scores
# A whole number n, then n names, then n scores (whole numbers). Print each name with its score, like:  Ada: 90
# Use zip.
# Example: 2, Ada, Bob, 90, 75 -> prints Ada: 90 / Bob: 75
n = int(input())
names = [input() for _ in range(n)]
scores = [int(input()) for _ in range(n)]
# --- your code below this line ---

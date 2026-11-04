# r8e1 - largest
# A whole number n (1 or more), then n whole numbers. Print the largest. Do not use max(); keep a running best.
# Example: 3, 4, 9, 2 -> prints 9
n = int(input())
# --- your code below this line ---
best = int(input())
for _ in range(n - 1):
    value = int(input())
    if value > best:
        best = value
print(best)

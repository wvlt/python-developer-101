# r5e2 — sum to
# A whole number n. Print the sum 1 + 2 + ... + n.
# Example: 4 -> prints 10
n = int(input())
# --- your code below this line ---
total = 0
for i in range(1, n + 1):
    total += i
print(total)

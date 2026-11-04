# r6e2 - skip threes
# A whole number n. Print 1 to n inclusive, one per line, but skip any number divisible by 3. Use continue.
# Example: 7 -> prints 1 / 2 / 4 / 5 / 7
n = int(input())
# --- your code below this line ---
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i)

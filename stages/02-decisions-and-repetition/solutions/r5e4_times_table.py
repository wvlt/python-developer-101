# r5e4 — times table
# A whole number n. Print its times table from 1 to 10, one line each, like:  3 x 4 = 12
# Example: 2 -> first line 2 x 1 = 2, last line 2 x 10 = 20
n = int(input())
# --- your code below this line ---
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

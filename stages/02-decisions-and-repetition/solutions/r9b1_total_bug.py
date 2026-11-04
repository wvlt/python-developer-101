# r9b1 — a planted bug (find it, fix it; ruff will help)
# A whole number n, then n whole numbers. Print their total, then the largest, on two lines.
# This program is complete and looks right; it even passes the first test. Run `just check 02` and read what
# ruff says about one of the names; rename it. Then run the tests: one still fails. Put print(f"{...=}") inside
# the loop and find out why. Fix it; do not rewrite it from scratch.
# Example: 3, 4, 9, 2 -> prints 15 then 9
n = int(input())
values = [int(input()) for _ in range(n)]  # the n numbers as a list (stage 3); you only need to fix what is below
# --- your code below this line ---
largest = values[0]
for v in values:
    if v > largest:
        largest = v
print(sum(values))
print(largest)

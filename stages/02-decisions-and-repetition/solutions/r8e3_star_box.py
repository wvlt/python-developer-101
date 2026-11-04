# r8e3 — star box
# Width w then height h (whole numbers, 1 or more). Print a rectangle of '*' that is w wide and h tall.
# Use a loop inside a loop; build each row with a loop, not with multiplication.
# Example: 3 and 2 -> prints *** / ***
w = int(input())
h = int(input())
# --- your code below this line ---
for _ in range(h):
    row = ""
    for _ in range(w):
        row += "*"
    print(row)

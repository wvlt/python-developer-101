# r2e1 — letter grade
# A score from 0 to 100. Print the letter: 85 or more A, 70 or more B, 55 or more C, 40 or more D, otherwise F.
# Example: 85 -> prints A
# Example: 39 -> prints F
score = int(input())
# --- your code below this line ---
if score >= 85:
    print("A")
elif score >= 70:
    print("B")
elif score >= 55:
    print("C")
elif score >= 40:
    print("D")
else:
    print("F")

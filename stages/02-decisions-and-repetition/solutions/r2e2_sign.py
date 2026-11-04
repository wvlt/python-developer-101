# r2e2 - sign
# A whole number. Print 'positive', 'negative' or 'zero'.
# Example: 3 -> prints positive
# Example: 0 -> prints zero
n = int(input())
# --- your code below this line ---
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

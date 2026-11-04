# r6e3 — is prime
# A whole number n (2 or more). Print 'prime' if nothing from 2 up to n-1 divides it, otherwise 'not prime'.
# Use a for loop with break, and else on the loop for the prime case.
# Example: 7 -> prints prime
# Example: 9 -> prints not prime
n = int(input())
# --- your code below this line ---
for d in range(2, n):
    if n % d == 0:
        print("not prime")
        break
else:
    print("prime")

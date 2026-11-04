# r5e3 - evens between
# Two whole numbers a and b, a <= b. Print the even numbers from a to b inclusive, one per line.
# Example: 3 and 8 -> prints 4 / 6 / 8
a = int(input())
b = int(input())
# --- your code below this line ---
for n in range(a, b + 1):
    if n % 2 == 0:
        print(n)

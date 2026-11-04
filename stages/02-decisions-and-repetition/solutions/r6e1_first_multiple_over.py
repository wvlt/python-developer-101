# r6e1 - first multiple over
# Two whole numbers: n (1 or more) and limit. Print the first multiple of n that is greater than limit.
# Count upwards from n with a loop and stop with break as soon as you pass the limit.
# Example: 7 and 100 -> prints 105
n = int(input())
limit = int(input())
# --- your code below this line ---
m = n
while True:
    if m > limit:
        print(m)
        break
    m += n

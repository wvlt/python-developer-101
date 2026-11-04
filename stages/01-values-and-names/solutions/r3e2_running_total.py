# r3e2 - running total
# Three whole numbers, one per line. Keep a running total and print it after each one (three lines).
# Example: 5, 10, 20 -> prints 5 then 15 then 35
a = int(input())
b = int(input())
c = int(input())
# --- your code below this line ---
total = 0
total += a
print(total)
total += b
print(total)
total += c
print(total)

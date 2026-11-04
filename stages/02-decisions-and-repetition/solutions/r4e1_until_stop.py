# r4e1 — until stop
# Lines of text arrive one at a time. Keep reading until a line says 'stop'. Then print how many lines came before it.
# Example: a, b, stop -> prints 2
# Example: stop -> prints 0
# --- your code below this line ---
count = 0
line = input()
while line != "stop":
    count += 1
    line = input()
print(count)

# r8e2 - count vowels
# A line of text. Print how many vowels (a e i o u, either case) it contains.
# Example: Hello World -> prints 3
text = input()
# --- your code below this line ---
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print(count)

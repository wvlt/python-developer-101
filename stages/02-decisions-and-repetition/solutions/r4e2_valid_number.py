# r4e2 — valid number
# Ask for a number from 1 to 10. Lines arrive one at a time. If a line is not made of digits, print
# 'not a number' and read the next. If it is a number outside 1-10, print 'out of range' and read the next.
# When a valid number arrives, print 'Got' and the number, and stop.
# Example: abc, 11, 5 -> prints  not a number / out of range / Got 5
# --- your code below this line ---
while True:
    text = input()
    if not text.isdigit():
        print("not a number")
    elif int(text) < 1 or int(text) > 10:
        print("out of range")
    else:
        print("Got", int(text))
        break

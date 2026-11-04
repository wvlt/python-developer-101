# r3e1 — weekday
# A number from 1 to 7. Print the day: 1 Monday, 2 Tuesday, 3 Wednesday, 4 Thursday, 5 Friday, 6 Saturday, 7 Sunday.
# Anything else: print 'unknown'. Use match/case.
# Example: 1 -> prints Monday
# Example: 9 -> prints unknown
n = int(input())
# --- your code below this line ---
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("unknown")

# Predict whether "done" is printed, in each of the two loops. F06.
for x in range(3):
    if x == 5:
        break
else:
    print("done A")
for x in range(3):
    if x == 1:
        break
else:
    print("done B")

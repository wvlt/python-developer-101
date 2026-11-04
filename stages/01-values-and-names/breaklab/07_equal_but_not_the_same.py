# Predict both. T05. (b is built at run time so Python cannot share the object.)
a = 1000
b = int("1000")
print(a == b)
print(a is b)

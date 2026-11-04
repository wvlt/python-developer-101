# r3e3 - rectangle
# Width then height, whole numbers. Print the area, then the perimeter, on two lines.
# Example: 3 and 4 -> prints 12 then 14
width = int(input())
height = int(input())
# --- your code below this line ---
area = width * height
perimeter = 2 * (width + height)
print(area)
print(perimeter)

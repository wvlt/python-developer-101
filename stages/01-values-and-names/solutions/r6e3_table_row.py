# r6e3 - table row
# An item name, a quantity (whole), a unit price (decimal). Print one row of a receipt:
# the name left-aligned in 10 characters, the quantity right-aligned in 3, the price right-aligned in 8
# with two decimal places. No separators between the columns.
# Example: apple, 3, 0.5 -> prints 'apple       3    0.50'
item = input()
qty = int(input())
price = float(input())
# --- your code below this line ---
print(f"{item:<10}{qty:>3}{price:>8.2f}")

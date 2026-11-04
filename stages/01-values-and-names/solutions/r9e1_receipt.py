# r9e1 — receipt (mini-project)
# Three items. For each: a name, a quantity (whole), a unit price (decimal), one per line; nine lines in all.
# Print a receipt:
#   a header line:  'Item      Qty   Price' (Item left in 10, Qty right in 3, Price right in 8 — exactly as r6e3)
#   one line per item, formatted as in r6e3, where Price is quantity times unit price
#   a line of 21 '-' characters
#   a last line with 'TOTAL' left-aligned in 13 characters and the total right-aligned in 8 with two decimals.
# Example input: apple 3 0.5 / bread 1 3.2 / milk 2 1.25  ->
# Item         Qty   Price
# apple       3    1.50
# bread       1    3.20
# milk        2    2.50
# ---------------------
# TOTAL            7.20
item1 = input()
qty1 = int(input())
price1 = float(input())
item2 = input()
qty2 = int(input())
price2 = float(input())
item3 = input()
qty3 = int(input())
price3 = float(input())
# --- your code below this line ---
line1 = qty1 * price1
line2 = qty2 * price2
line3 = qty3 * price3
total = line1 + line2 + line3
print(f"{'Item':<10}{'Qty':>3}{'Price':>8}")
print(f"{item1:<10}{qty1:>3}{line1:>8.2f}")
print(f"{item2:<10}{qty2:>3}{line2:>8.2f}")
print(f"{item3:<10}{qty3:>3}{line3:>8.2f}")
print("-" * 21)
print(f"{'TOTAL':<13}{total:>8.2f}")

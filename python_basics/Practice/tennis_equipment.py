from math import floor
from math import ceil
tennis_raquet_price = float(input())
tennis_raquet_qty = int(input())
sneakers_qty = int(input())

sneakers_price = tennis_raquet_price / 6
other_equipment = 0.2 * ((tennis_raquet_price * tennis_raquet_qty)+(sneakers_qty * sneakers_price))

total_price = (tennis_raquet_price * tennis_raquet_qty) + (sneakers_qty * sneakers_price) + other_equipment

print(f"Price to be paid by Djokovic {floor(total_price / 8)}")
print(f"Price to be paid by sponsors {ceil(7/8 * total_price)}")




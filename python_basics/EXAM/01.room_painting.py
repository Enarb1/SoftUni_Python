from math import ceil
from math import floor
BOX_OF_PAINT = 21.50
TAPET_ROLL = 5.20

box_of_paint_qty = int(input())
tapet_qty = int(input())
gloves_per_item_price = float(input())
brush_per_item_price = float(input())

gloves_qty = ceil(0.35 * tapet_qty)
brush_qty = floor(0.48 * box_of_paint_qty)

total_cost = (BOX_OF_PAINT * box_of_paint_qty) + (TAPET_ROLL * tapet_qty) + (gloves_per_item_price * gloves_qty) + (brush_per_item_price * brush_qty)

delivery = 1/15 * (total_cost)

print(f"This delivery will cost {delivery:.2f} lv.")
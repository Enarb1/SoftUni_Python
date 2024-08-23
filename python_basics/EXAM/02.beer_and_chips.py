from math import ceil

name = input()
budget = float(input())
beers_qty = int(input())
chips_qty = int(input())


BEER_PRICE_PER_ITEM = 1.20
beers_total = BEER_PRICE_PER_ITEM * beers_qty
CHIPS_PER_ITEM_PRICE = 0.45 * beers_total
chips_total = ceil(CHIPS_PER_ITEM_PRICE * chips_qty)

total_price = chips_total + beers_total

if budget >= total_price:
    print(f"{name} bought a snack and has {abs(budget - total_price):.2f} leva left.")
else:
    print(f"{name} needs {abs(budget - total_price):.2f} more leva!")
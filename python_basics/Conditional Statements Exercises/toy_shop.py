PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

trip_price = float(input())

puzzle_qty = int(input())
talking_dolls_qty = int(input())
teddy_bear_qty = int(input())
minion_qty = int(input())
truck_qty = int(input())

total_qty = puzzle_qty + talking_dolls_qty + teddy_bear_qty + minion_qty + truck_qty
total_price = (puzzle_qty * PUZZLE_PRICE) + (talking_dolls_qty * TALKING_DOLL_PRICE) + (teddy_bear_qty * TEDDY_BEAR_PRICE) + (minion_qty * MINION_PRICE) + (truck_qty * TRUCK_PRICE)

if total_qty >= 50:
    total_price = total_price - (total_price * 0.25)
    total_price = total_price - (total_price * 0.10)
else:
    total_price = total_price - (total_price * 0.10)

if total_price >= trip_price:
    print(f'Yes! {total_price - trip_price:.2f} lv left.')
else:
    print( f'Not enough money! {trip_price - total_price:.2f} lv needed.')
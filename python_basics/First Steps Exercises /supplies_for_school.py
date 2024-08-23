PENS_PRICE = 5.8
MARKER_PRICE = 7.2
CLEANER_PER_LIT = 1.2

pens_qty = int(input())
marker_qty = int(input())
cleaner_qty= int(input())

discount = int(input())

total_price = (pens_qty * PENS_PRICE) + (marker_qty * MARKER_PRICE) + (cleaner_qty * CLEANER_PER_LIT)
discount_price = total_price - (total_price * (discount/100))

print(discount_price)
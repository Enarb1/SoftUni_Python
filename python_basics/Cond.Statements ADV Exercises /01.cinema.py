screening_type = input()
rows = int(input())
columns = int(input())

PREMIERE_TICKET_PRICE = 12.00
NORMAL_TICKET_PRICE = 7.50
DISCOUNT_TICKET_PRICE = 5.00

capacity = rows * columns
income = 0

if screening_type == "Premiere":
    income = capacity * PREMIERE_TICKET_PRICE
elif screening_type == "Normal":
    income = capacity * NORMAL_TICKET_PRICE
elif screening_type == "Discount":
    income = capacity * DISCOUNT_TICKET_PRICE

print(f"{income:.2f} leva")


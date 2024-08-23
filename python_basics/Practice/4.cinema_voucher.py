voucher_price = int(input())

tickets_bought = 0
other_stuff_bought = 0


while True:
    purchase = input()
    if purchase == "End" or voucher_price <= 0:
        break
    else:
        if len(purchase) > 8:
            purchase_price = ord(purchase[0]) + ord(purchase[1])
        else:
            purchase_price = ord(purchase[0])

        if voucher_price >= purchase_price:
            if len(purchase) > 8:
                tickets_bought += 1
            else:
                other_stuff_bought += 1
            voucher_price -= purchase_price
        else:
            break

print(f"{tickets_bought}")
print(f"{other_stuff_bought}")

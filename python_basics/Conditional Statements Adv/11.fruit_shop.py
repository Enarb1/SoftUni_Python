fruit = input()
day = input()
qty = float(input())

product_price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == 'Thursday' or day == 'Friday':
    if fruit == "banana":
        product_price = 2.50
    elif fruit == 'apple':
        product_price = 1.20
    elif fruit == 'orange':
        product_price = 0.85
    elif fruit == 'grapefruit':
        product_price = 1.45
    elif fruit == 'kiwi':
        product_price = 2.70
    elif fruit == 'pineapple':
        product_price = 5.50
    elif fruit == 'grapes':
        product_price = 3.85
    else:
        print('error')
        exit()
elif day == 'Saturday' or day == 'Sunday':
    if fruit == "banana":
        product_price = 2.70
    elif fruit == 'apple':
        product_price = 1.25
    elif fruit == 'orange':
        product_price = 0.90
    elif fruit == 'grapefruit':
        product_price = 1.60
    elif fruit == 'kiwi':
        product_price = 3.00
    elif fruit == 'pineapple':
        product_price = 5.60
    elif fruit == 'grapes':
        product_price = 4.20
    else:
        print('error')
        exit()
else:
    print('error')
    exit()

total_sum = product_price * qty

print(f"{total_sum:.2f}")

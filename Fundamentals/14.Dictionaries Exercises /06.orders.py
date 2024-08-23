stock = {}

while True:
    command = input()
    if command == 'buy':
        break
    product_input = command.split()
    product = product_input[0]
    price = float(product_input[1])
    quantity = int(product_input[2])

    if product not in stock:
        stock[product] = {}
        stock[product]['price'] = price
        stock[product]['quantity'] = 0
    stock[product]['quantity'] += quantity
    stock[product]['price'] = price


for product,details in stock.items():
    price = details['price']
    quantity = details['quantity']
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")

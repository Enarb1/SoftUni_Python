products = {}
command = input()

while command != 'statistics':
    items = command.split(": ")
    product = items[0]
    quantity = int(items[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity
    command = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
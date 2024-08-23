input_list = input().split()
searched_products = input().split()
stock = {}

for index in range(0, len(input_list), 2):
    product = input_list[index]
    quantity = int(input_list[index + 1])
    stock[product] = quantity

for product in searched_products:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

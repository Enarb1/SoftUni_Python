def receive(qty, food, foods_dict, sold_quantities):

    if food not in foods_dict.items():
        foods_dict[food] = 0
    foods_dict[food] += int(qty)


def sell(qty, food, foods_dict, sold_quantities):

    if foods_dict[food] < int(qty):
        food_quantity = foods_dict[food]
        sold_quantities.append(food_quantity)
        print(f"There aren't enough {food}. You sold the last {food_quantity} of them.")
        del foods_dict[food]
    else:
        foods_dict[food] -= int(qty)
        sold_quantities.append(int(qty))
        print(f"You sold {qty} {food}.")
        if foods_dict[food] == 0:
            del foods_dict[food]


foods = {}
sold_qtys =[]

while True:
    command = input()
    if command == 'Complete':
        break

    action, quantity, food_type = command.split()
    if action == 'Receive':
        if not int(quantity) <= 0:
            receive(quantity, food_type, foods, sold_qtys)
    elif action == 'Sell':
        if food_type not in foods.keys():
            print(f'You do not have any {food_type}.')
        else:
            sell(quantity, food_type, foods, sold_qtys)

for food, qtys in foods.items():
    print(f'{food}: {qtys}')
print(f"All sold: {sum(sold_qtys)} goods")
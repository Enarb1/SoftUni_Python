TICKET_TO_PARIS = 150
items_list = input().split("|")
budget = float(input())
items_initial_price_total = 0
bought_items = []

for product in items_list:
    item_and_price = product.split("->")
    item = item_and_price[0]
    price = float(item_and_price[1])
    if budget >= price:
        if item == "Clothes" and price <= 50.00:
            budget -= price
            items_initial_price_total += price
            sale_price = price + (price * 0.40)
            bought_items.append(float("%.2f" % sale_price))
        elif item == "Shoes" and price <= 35.00:
            budget -= price
            items_initial_price_total += price
            sale_price = price + (price * 0.40)
            bought_items.append(float("%.2f" % sale_price))
        elif item == "Accessories" and price <= 20.50:
            budget -= price
            items_initial_price_total += price
            sale_price = price + (price * 0.40)
            bought_items.append(float("%.2f" % sale_price))
budget += sum(bought_items)
profit = sum(bought_items) - items_initial_price_total
for element in bought_items:
    print(f"{element:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget >= TICKET_TO_PARIS:
    print("Hello, France!")
else:
    print("Not enough money.")



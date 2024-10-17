def final_print(budget, grocery_list):

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


def shop_from_grocery_list(budget, grocery_list, *products_prices):

    for product, price in products_prices:
        if price > budget:
            break
        if product in grocery_list and price <= budget:
            budget -= price
            grocery_list.remove(product)

    return final_print(budget, grocery_list)


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
def shopping_cart(*meals):
    limits = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }

    prepared = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    for command in meals:
        if command == "Stop":
            break

        meal, product = command[0], command[1]
        if len(prepared[meal]) < limits[meal] and product not in prepared[meal]:
            prepared[meal].append(product)

    sorted_meals = sorted(prepared.items(), key=lambda x: (-len(x[1]), x[0]))

    message = ""
    if all(len(m) == 0 for m in prepared.values()):
        message += "No products in the cart!"
    else:
        for dish, products in sorted_meals:
            message += f"{dish}:\n"
            if prepared[dish]:
                message += '\n'.join(f" - {prod}" for prod in sorted(prepared[dish])) + "\n"

    return message



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

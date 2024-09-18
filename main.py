def print_result(cuisines):
    result = []

    for cus_n, recept in cuisines.items():
        result.append(f"{cus_n} cuisine contains {len(cuisines[cus_n])} recipes:")
        for rcpt_n, ingr in recept.items():
            result.append(f"  * {rcpt_n} -> Ingredients: {', '.join(ingr)}")

    return result


def get_cuisines(*info):
    cuisines = {}

    for elements in sorted(info):
        recept_name, cuisine_name, ingredients = elements
        if cuisine_name not in cuisines:
            cuisines[cuisine_name] = {}
        cuisines[cuisine_name][recept_name] = ingredients

    return dict(sorted(cuisines.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))


def cookbook(*recopies):
    cuisines = get_cuisines(*recopies)
    final_print = print_result(cuisines)

    return '\n'.join(final_print)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
def sorting_cheeses(**kwargs):

    sorted_cheese = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""
    for cheese, quantities in sorted_cheese:
        result += f"{cheese}\n"
        reversed_qty = sorted(quantities, reverse=True)
        for quantity in reversed_qty:
            result += f"{quantity}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
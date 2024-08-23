def grocery_store(**products_data):
    products_data = sorted(products_data.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    return '\n'.join(f"{product}: {qty}" for product, qty in products_data)
    # result = []
    #
    # for product, qty in products_data:
    #     result.append(f"{product}: {qty}")
    #
    # return '\n'.join(result)



print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
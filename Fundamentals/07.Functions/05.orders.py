
def bill(product, quantity):
    total = 0
    if product == "coffee":
        total = quantity * 1.50
    elif product == "water":
        total = quantity * 1.00
    elif product == "coke":
        total = quantity * 1.40
    elif product == "snacks":
        total = quantity * 2.00

    return total


product_type = input()
product_quantity = int(input())
result = bill(product_type,product_quantity)
print(f"{result:.2f}")
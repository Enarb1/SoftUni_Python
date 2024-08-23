product = input()
city = input()
qty = float(input())

product_price = 0

if city == "Sofia":
    if product == 'coffee':
        product_price = 0.50
    if product == "water":
        product_price = 0.80
    if product == "beer":
        product_price = 1.20
    if product == "sweets":
        product_price = 1.45
    if product == "peanuts":
        product_price = 1.60

if city == "Plovdiv" :
    if product == 'coffee':
        product_price = 0.40
    if product == "water":
        product_price = 0.70
    if product == "beer":
        product_price = 1.15
    if product == "sweets":
        product_price = 1.30
    if product == "peanuts":
        product_price = 1.50
if city == "Varna":
    if product == 'coffee':
        product_price = 0.45
    if product == "water":
        product_price = 0.70
    if product == "beer":
        product_price = 1.10
    if product == "sweets":
        product_price = 1.35
    if product == "peanuts":
        product_price = 1.55

total_price = product_price * qty

print(total_price)

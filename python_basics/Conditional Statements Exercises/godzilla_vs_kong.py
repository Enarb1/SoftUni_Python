budget = float(input())
extras_qty = int(input())
clothing_price_per_extra = float(input())

decore = budget * 0.1
clothing_extras_total = extras_qty * clothing_price_per_extra

if extras_qty > 150 :
    clothing_extras_total = clothing_extras_total * 0.9

total_cost = decore + clothing_extras_total
difference = abs(total_cost-budget) # тук използваме abs за да изкараме абсолщртната стойност. премахва знака минус 

if total_cost > budget :
    print("Not enough money!")
    print(f" Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
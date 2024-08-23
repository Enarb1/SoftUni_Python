CAT_FOOD_PER_KG = 12.45

cats_qty = int(input())
group1 = 0
group2 = 0
group3 = 0
total_food_weight = 0

for _ in range(cats_qty):
    food_weight = float(input())

    if 100 <= food_weight < 200:
        group1 += 1
        total_food_weight += food_weight
    elif 200 <= food_weight < 300:
        group2 += 1
        total_food_weight += food_weight
    else:
        group3 += 1
        total_food_weight += food_weight

total_price = (total_food_weight / 1000) * CAT_FOOD_PER_KG

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
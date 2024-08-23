DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4

dog_food_qty = int(input())
cat_food_qty = int(input())

total_sum = (DOG_FOOD_PRICE * dog_food_qty) + (CAT_FOOD_PRICE * cat_food_qty)

print(f'{total_sum} lv.')
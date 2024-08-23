import re

text_input = input()

pattern = r'([#|])([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})\1'
matches = re.finditer(pattern, text_input)
foods = []
total_cals = 0

for match in matches:
    food = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))
    foods.append({'name': food, 'exp': date, 'cals': calories})
    total_cals += calories

enough_food_for = total_cals // 2000
print(f'You have food to last you for: {enough_food_for} days!')
for item in foods:
    print(f'Item: {item["name"]}, Best before: {item["exp"]}, Nutrition: {item["cals"]}')

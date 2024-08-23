def month(food_total_kg, hay_total_kg, cover_total_kg,weight_pig_kg):

    for day in range(1, 31):
        food_total_kg -= 0.300
        if day % 2 == 0:
            hay_total_kg -= 0.05 * food_total_kg
        if day % 3 == 0:
            cover_total_kg -= 1/3 * pig_weight_kg
        if int(food_total_kg) <= 0 or int(hay_total_kg) <= 0 or int(cover_total_kg) <= 0:
            return f"Merry must go to the pet store!"
    return f"Everything is fine! Puppy is happy! Food: {food_total_kg:.2f}, Hay: {hay_total_kg:.2f}, Cover: {cover_total_kg:.2f}."


total_food_kg = float(input())
total_hay_kg = float(input())
total_cover_kg = float(input())
pig_weight_kg = float(input())

print(month(total_food_kg, total_hay_kg, total_cover_kg, pig_weight_kg))

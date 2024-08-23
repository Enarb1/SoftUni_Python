food = int(input()) * 1000

total_food = 0

while True:
    command = input()
    if command == "Adopted":
        break
    else:
        grams_food = int(command)
        total_food += grams_food


if total_food <= food:
    print(f"Food is enough! Leftovers: {food - total_food} grams.")

else:
    print(f"Food is not enough. You need {abs(food - total_food)} grams more.")




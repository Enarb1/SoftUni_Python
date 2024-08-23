budget = int(input())
season = input()
people = int(input())

boat_rental = 0

if season == "Spring":
    boat_rental = 3000
    if people <= 6:
        boat_rental *= 0.9
    elif 7 <= people <= 11:
        boat_rental *= 0.85
    else:
        boat_rental *= 0.75

elif season == "Summer" or season == "Autumn":
    boat_rental = 4200
    if people <= 6:
        boat_rental *= 0.9
    elif 7 <= people <= 11:
        boat_rental *= 0.85
    else:
        boat_rental *= 0.75
else:
    boat_rental = 2600
    if people <= 6:
        boat_rental *= 0.9
    elif 7 <= people <= 11:
        boat_rental *= 0.85
    else:
        boat_rental *= 0.75

if season != "Autumn" and people % 2 == 0:
    boat_rental *= 0.95
if budget >= boat_rental:
    print(f"Yes! You have {budget-boat_rental:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rental-budget:.2f} leva.")

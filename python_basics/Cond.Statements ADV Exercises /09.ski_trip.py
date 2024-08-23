stays_days = int(input())
room_type = input()
grade = input()

ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

nights = stays_days - 1
total_price = 0

if room_type == "room for one person":
    total_price = nights * ROOM_FOR_ONE_PERSON
elif room_type == "apartment":
    total_price = nights * APARTMENT
    if nights < 10:
        total_price *= 0.70
    elif nights >= 10 and nights <= 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.50
elif room_type == "president apartment":
    total_price = nights * PRESIDENT_APARTMENT
    if nights < 10:
        total_price *= 0.90
    elif nights >= 10 and nights <= 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.80
if grade == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90
if nights < 1:
    total_price = 0

print(f"{total_price:.2f}")
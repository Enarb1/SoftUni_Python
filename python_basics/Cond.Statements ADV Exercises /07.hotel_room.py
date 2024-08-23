month = input()
days = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if days > 14:
        apartment_price *= 0.9
        studio_price *= 0.70
    elif days > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        apartment_price *= 0.9
        studio_price *= 0.80
else:
    apartment_price = 77
    studio_price = 76
    if days > 14:
        apartment_price *= 0.9

print(f"Apartment: {days * apartment_price:.2f} lv.")
print(f"Studio: {days * studio_price:.2f} lv.")



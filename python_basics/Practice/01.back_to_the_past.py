inherited_money = float(input())
year_to_live = int(input())
years = 18
money = 0

for year in range(1800,year_to_live + 1):
    if year % 2 == 0:
        money += 12000
    elif year % 2 != 0:
        money += 12000 + (50 * years)
    years += 1
if money <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {inherited_money - money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money - money):.2f} dollars to survive.")







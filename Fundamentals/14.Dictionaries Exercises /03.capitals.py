countries = input().split(", ")
capitals = input().split(", ")

country_capital = dict(zip(countries, capitals))

for country, capital in country_capital.items():
    print(f"{country} -> {capital}")
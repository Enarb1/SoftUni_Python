number_of_cities = int(input())
visited_cities = 0
total_profit = 0

while number_of_cities > 0:
    city = input()
    income = float(input())
    expense = float(input())
    profit = income - expense
    visited_cities += 1
    if visited_cities % 3 == 0:
        if visited_cities % 5 == 0:
            pass
        else:
            profit -= 0.5 * expense
    if visited_cities % 5 == 0:
        profit -= 0.1 * income
    total_profit += profit
    number_of_cities -= 1
    print(f"In {city} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")





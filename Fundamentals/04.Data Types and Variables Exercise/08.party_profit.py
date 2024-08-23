group = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        group -= 2
    if current_day % 15 == 0:
        group += 5
    if current_day % 3 == 0:
        coins -= 3 * group
    if current_day % 5 == 0:
        coins += 20 * group
        if current_day % 3 == 0:
            coins -= 2 * group
    coins += 50
    coins -= 2 * group
print(f"{group} companions received {int(coins / group)} coins each.")
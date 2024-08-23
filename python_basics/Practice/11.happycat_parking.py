days = int(input())
hours = int(input())

day_counter = 0
total_sum = 0

for day in range(1, days + 1):
    day_counter += 1
    day_total = 0
    for hour in range(1, hours + 1):
        price = 0
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
        else:
            price += 1
        day_total += price
        total_sum += price
    print(f"Day: {day_counter} - {day_total:.2f} leva")
print(f"Total: {total_sum:.2f} leva")
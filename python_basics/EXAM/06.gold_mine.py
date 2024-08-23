locations = int(input())

for _ in range(locations):
    expected_average = float(input())
    days_at_location = int(input())
    total_gold = 0
    average_gold = total_gold / days_at_location

    for _ in range(days_at_location):
        gold = float(input())
        total_gold += gold

    average_gold = total_gold / days_at_location

    if average_gold >= expected_average:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {expected_average - average_gold:.2f} gold.")

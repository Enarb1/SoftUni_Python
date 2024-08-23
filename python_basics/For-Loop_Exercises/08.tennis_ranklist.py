from math import floor

tournaments = int(input())
starting_points = int(input())

tournaments_won = 0
gained_points = 0

for _ in range(tournaments):
    result = input()
    if result == "W":
        tournaments_won += 1
        gained_points += 2000
    elif result == "F":
        gained_points += 1200
    elif result == "SF":
        gained_points += 720

print(f"Final points: {starting_points + gained_points}")
print(f"Average points: {floor(gained_points / tournaments)}")
print(f"{tournaments_won / tournaments * 100:.2f}%")


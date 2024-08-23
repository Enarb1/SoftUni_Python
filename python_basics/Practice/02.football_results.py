wins = 0
draws = 0
lost = 0

for _ in range(3):
    match_result = input()
    goals = match_result.split(":")
    team_goals = int(goals[0])
    opponent_goals = int(goals[1])

    if team_goals > opponent_goals:
        wins += 1
    elif team_goals == opponent_goals:
        draws += 1
    else:
        lost += 1
print(f"Team won {wins} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draws}")




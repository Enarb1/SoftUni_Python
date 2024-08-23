input_string = input()
sanctioned_players_list = input_string.split(" ")
updated_sanctioned_players_lst = []
team_a = 11
team_b = 11
game_terminated = False
for item in sanctioned_players_list:
    if item not in updated_sanctioned_players_lst:
        updated_sanctioned_players_lst.append(item)
for player in updated_sanctioned_players_lst:
    if player[0] == "A":
        team_a -= 1
    else:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
def team_lineup(*player_info):
    teams = {}

    for player, nation in player_info:
        if nation not in teams.keys():
            teams[nation] = []
        teams[nation].append(player)

    sorted_teams = sorted(teams.items(),key=lambda kvp: (-len(kvp[1]),kvp[0]))

    print_result = ''

    for country, players in sorted_teams:
        print_result += f"{country}:\n"
        print_result += '\n'.join(f"  -{p}" for p in players) + '\n'

    return print_result
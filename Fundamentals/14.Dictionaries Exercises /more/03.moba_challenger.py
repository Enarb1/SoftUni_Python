def add_player(players_pool, player,position, skill):
    if player not in players_pool.keys():
        players_pool[player] = {}
    if position not in players_pool[player].keys() or players_pool[player][position] < skill:
        players_pool[player][position] = skill


def duel(players_pool, player_one, player_two):
    player_one_total = 0
    player_two_total = 0
    looser = ''

    if player_one in players_pool.keys() and player_two in players_pool.keys():
        for position_one, skill_one in players_pool[player_one].items():
            for position_two, skill_two in players_pool[player_two].items():
                if position_one == position_two:
                    player_one_total += int(skill_one)
                    player_two_total += int(skill_two)
        if player_one_total > player_two_total:
            looser = player_two
        elif player_two_total > player_one_total:
            looser = player_one
        else:
            pass
    if looser:
        players_pool.pop(looser)


def season_end():
    sorted_players = sorted(players_pool.items(), key=lambda player_pos: (-sum(player_pos[1].values()), player_pos[0]))

    for player, positions in sorted_players:
        print(f'{player}: {sum(positions.values())} skill')
        sorted_positions = sorted(positions.items(), key=lambda pos: (-pos[1], pos[0]))
        for position, skill in sorted_positions:
            print(f'- {position} <::> {skill}')


players_pool = {}

while True:
    command = input()
    if command == 'Season end':
        season_end()
        break

    if ' -> ' in command:
        info = command.split(" -> ")
        player = info[0]
        position = info[1]
        skill = int(info[2])
        add_player(players_pool, player, position, skill)
    elif ' vs ' in command:
        info = command.split(" vs ")
        player_one = info[0]
        player_two = info[1]
        duel(players_pool, player_one, player_two)






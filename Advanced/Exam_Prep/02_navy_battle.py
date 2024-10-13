BATTLE_CRUISERS = 3
MAX_HITS = 3

def dash(matrix, my_pos):
    matrix[my_pos[0]][my_pos[1]] = "-"
    return matrix

def get_battlefield(size):
    matrix = []
    my_pos = []
    for row in range(size):
        line = [el for el in input()]
        if "S" in line:
            my_pos = [row, line.index("S")]
        matrix.append(line)
    dash(matrix,my_pos)

    return  matrix, my_pos

def navy_battle():
    n = int(input())

    directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
    }

    battlefield, ship_pos = get_battlefield(n)
    enemies_left = BATTLE_CRUISERS
    mine_hits = 0

    while True:
        direction = input()
        ship_pos = [ship_pos[0] + directions[direction][0], ship_pos[1] + directions[direction][1]]

        if battlefield[ship_pos[0]][ship_pos[1]] == "*":
            dash(battlefield,ship_pos)
            mine_hits += 1
        if mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{ship_pos[0]}, {ship_pos[1]}]!")
            break
        if battlefield[ship_pos[0]][ship_pos[1]] == "C":
            dash(battlefield,ship_pos)
            enemies_left -= 1
        if enemies_left == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
            
    battlefield[ship_pos[0]][ship_pos[1]] = "S"
    print(*[''.join(r) for r in battlefield], sep='\n')

navy_battle()

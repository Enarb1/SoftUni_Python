def movement(player_position,stars, direction):
    r = player_position[0] + directions[direction][0]
    c = player_position[1] + directions[direction][1]

    if not 0 <= r < size or not 0 <= c < size:
        r, c = 0, 0

    if not field[r][c] == "#":
        player_position = [r, c]
        if field[r][c] == "*":
            stars += 1
            field[r][c] = "."
    else:
        stars -= 1

    return player_position, stars


size = int(input())

field = []
stars_total = 2
player_pos = None


for i in range(size):
    line = input().split()
    if "P" in line:
        player_pos = [i, line.index("P")]
    field.append(line)

field[player_pos[0]][player_pos[1]] = "."

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


while True:

    if stars_total == 0 or stars_total == 10:
        break

    command = input()
    player_pos, stars_total = movement(player_pos,stars_total, command)


field[player_pos[0]][player_pos[1]] = "P"

if stars_total >= 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is {player_pos}")
print(*[' '.join(row) for row in field], sep="\n")
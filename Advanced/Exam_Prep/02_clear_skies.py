SIZE = int(input())


def player_movement(player_position, direction):

    row = player_position[0] + directions[direction][0]
    col = player_position[1] + directions[direction][1]

    return [row, col]


directions ={
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

armour = 300
enemies = 4

airspace = []
plane_pos = []

for r in range(SIZE):
    line = list(input())
    airspace.append(line)
    if "J" in line:
        plane_pos = [r, line.index("J")]
        airspace[plane_pos[0]][plane_pos[1]] = "-"

while armour > 0 and enemies > 0:
    movement_direction = input()
    plane_pos = player_movement(plane_pos, movement_direction)

    if airspace[plane_pos[0]][plane_pos[1]] == "E":
        enemies -= 1
        if enemies:
            armour -= 100
    elif airspace[plane_pos[0]][plane_pos[1]] == "R":
        armour = 300

    airspace[plane_pos[0]][plane_pos[1]] = "-"

if enemies:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates {plane_pos}!")
else:
    print("Mission accomplished, you neutralized the aerial threat!")

airspace[plane_pos[0]][plane_pos[1]] = "J"
print(*[''.join(row) for row in airspace], sep='\n')
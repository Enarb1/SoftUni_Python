def position(direction):
    row = bee_position[0] + directions[direction][0]
    col = bee_position[1] + directions[direction][1]

    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    return [row, col]


def move(matrix, direction, bee_pos, energy, collected_nectar):
    n = len(matrix)
    bee_pos = position(direction)
    x, y = bee_pos

    energy -= 1

    if field[x][y].isdigit():
        collected_nectar += int(field[x][y])
        field[x][y] = '-'

    return [x, y], energy, collected_nectar


size = int(input().strip())
field = []

NECTAR_GOAL = 30
energy_left = 15
bee_position = None
nectar_collected = 0
restored_energy = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(size):
    field.append(list(input().strip()))
    if "B" in field[i]:
        bee_position = [i, field[i].index("B")]
        field[i][bee_position[1]] = "-"

while True:
    command = input().strip()
    bee_position, energy_left, nectar_collected = move(field, command, bee_position, energy_left, nectar_collected)
    r, c = bee_position

    if field[r][c] == "H":
        if nectar_collected >= NECTAR_GOAL:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy_left}")
            break
        else:
            print("Beesy did not manage to collect enough nectar.")
            break

    if energy_left <= 0:
        if nectar_collected >= 30 and not restored_energy:
            restored_energy = True
            energy_left += nectar_collected - NECTAR_GOAL
            collected_nectar = 30
        else:
            print("This is the end! Beesy ran out of energy.")
            break

field[bee_position[0]][bee_position[1]] = "B"
print(*[''.join(row) for row in field], sep="\n")

rows, cols = [int(x) for x in input().split()]
matrix = []
player_pos = []
final_pos = []
bunnies = set()
directions = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

valid_rows = range(rows)
valid_cols = range(cols)

for row in range(rows):
    matrix.append([el for el in input()])

    if 'P' in matrix[row]:
        player_pos = [row, matrix[row].index('P')]
    if 'B' in matrix[row]:
        bunnies.add((row, matrix[row].index('B')))

commands = [el for el in input()]
dead = False
for command in commands:
    r, c = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
    matrix[player_pos[0]][player_pos[1]] = '.'

    if not (0 <= r < rows and 0 <= c < cols):
        final_pos = player_pos
        player_pos = []
    else:
        player_pos = [r, c]
        matrix[player_pos[0]][player_pos[1]] = 'P'

        if matrix[r][c] == 'B':
            dead = True
            break

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                bunnies.add((row, col))

    for bunnie_pos in bunnies:
        x, y = bunnie_pos[0], bunnie_pos[1]

        if {y + 1}.issubset(valid_cols):
            matrix[x][y + 1] = 'B'
        if {y - 1}.issubset(valid_cols):
            matrix[x][y - 1] = 'B'
        if {x - 1}.issubset(valid_rows):
            matrix[x - 1][y] = 'B'
        if {x + 1}.issubset(valid_rows):
            matrix[x + 1][y] = 'B'

    if not player_pos:
        break

    if matrix[player_pos[0]][player_pos[1]] == 'B':
        dead = True
        break


[print(*row, sep='') for row in matrix]

if dead:
    print(f"dead: {player_pos[0]} {player_pos[1]}")
else:
    print(f"won: {final_pos[0]} {final_pos[1]}")


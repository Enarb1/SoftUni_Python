def movement(direction):
    row = player_pos[0] + directions[direction][0]
    col = player_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        return player_pos

    return [row, col]


size = int(input())

player_pos = []
maze = []

MONSTER_DAMAGE = 40
HEALTH_POTION = 15

health_total = 100
dead = False
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(size):
    maze.append(list(input()))
    if "P" in maze[r]:
        player_pos = [r, maze[r].index('P')]
        maze[player_pos[0]][player_pos[1]] = '-'

while not dead:
    command = input()

    player_pos = movement(command)

    if maze[player_pos[0]][player_pos[1]] == "M":
        health_total -= MONSTER_DAMAGE
        if health_total <= 0:
            health_total = 0
            dead = True
        if not dead:
            maze[player_pos[0]][player_pos[1]] = "-"
    elif maze[player_pos[0]][player_pos[1]] == "H":
        health_total += HEALTH_POTION
        maze[player_pos[0]][player_pos[1]] = "-"
        if health_total > 100:
            health_total = 100
    elif maze[player_pos[0]][player_pos[1]] == "X":
        break

maze[player_pos[0]][player_pos[1]] = "P"

if dead:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")
print(f"Player's health: {health_total} units")

print(*[''.join(row) for row in maze], sep='\n')
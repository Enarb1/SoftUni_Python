OTHER_PLAYERS = 3

def final_print(moves, touched_opponents):
    return f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}"

def obstacle(playground, r, c):
    return playground[r][c] == "O"

def valid_position(rows, cols, row,col):
    return 0 <= row < rows and 0 <= col < cols

def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

def get_playground_and_start_pos(rows):
    matrix = []
    my_pos = []

    for row in range(rows):
        line = input().split()
        if "B" in line:
            my_pos = [row, line.index("B")]
        matrix.append(line)

    return matrix, my_pos

def blind_mans_buff(rows, cols):
    playground, my_position = get_playground_and_start_pos(rows)
    directions = directions_mapper()
    moves = 0
    players_touched = 0

    while True:
        command = input()
        if command == "Finish":
            break
        direction = command

        r = directions[direction][0] + my_position[0]
        c = directions[direction][1] + my_position[1]

        if not valid_position(rows, cols, r,c) or obstacle(playground, r, c):
            continue

        my_position = [r, c]
        moves += 1
        if playground[r][c] == "P":
            players_touched += 1

        playground[r][c] = "-"
        if players_touched == OTHER_PLAYERS:
            break

    return final_print(moves,players_touched)


n, m = map(int, input().split())
print(blind_mans_buff(n, m))
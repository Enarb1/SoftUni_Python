STARTING_SECONDS = 16

def final_print(terrorist_win, bomb_is_defused, exploded, defuse_command, bomb_pos, my_pos, seconds_left):
    if terrorist_win:
        print("Terrorists win!")
        if defuse_command:
            print("Bomb was not defused successfully!")
            if my_pos != bomb_pos:
                print(f"Time needed: 0 second/s.")
            else:
                print(f"Time needed: {abs(seconds_left)} second/s.")
    elif exploded:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(seconds_left)} second/s.")
    else:
        print("Counter-terrorist wins!")
        print(f"Bomb has been defused: {seconds_left} second/s remaining.")


def defusing_successful(seconds_left):
    return seconds_left >= 0


def defuse_possible(bomb_pos, my_pos):
    return bomb_pos == my_pos


def valid_position(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }


def get_matrix(rows):
    matrix = []
    starting_pos = []
    bomb_pos = []

    for row in range(rows):
        line = [el for el in input()]
        if "C" in line:
            starting_pos = [row, line.index("C")]
        if "B" in line:
            bomb_pos = [row, line.index("B")]
        matrix.append(line)

    return matrix, starting_pos, bomb_pos


def counter_strike(rows, cols):
    battlefield, start_pos, bomb_pos = get_matrix(rows)

    counter_terror_pos = start_pos
    directions = directions_mapper()

    seconds_left = STARTING_SECONDS
    bomb_is_defused = False
    exploded = False
    terrorist_win = False
    defuse_command = False

    while True:
        if terrorist_win or bomb_is_defused or exploded:
            break

        if seconds_left <= 0:
            exploded = True
            break

        command = input()

        if command == "defuse":
            defuse_command = True
            if defuse_possible(bomb_pos, counter_terror_pos):
                seconds_left -= 4
                if defusing_successful(seconds_left):
                    bomb_is_defused = True
                    battlefield[counter_terror_pos[0]][counter_terror_pos[1]] = "D"
                else:
                    exploded = True
                    terrorist_win = True
                    battlefield[counter_terror_pos[0]][counter_terror_pos[1]] = "X"
            else:
                seconds_left -= 2
        else:
            seconds_left -= 1
            direction = command

            r = counter_terror_pos[0] + directions[direction][0]
            c = counter_terror_pos[1] + directions[direction][1]

            if valid_position(r, c, rows, cols):
                counter_terror_pos = [r, c]

                if battlefield[counter_terror_pos[0]][counter_terror_pos[1]] == "T":
                    battlefield[counter_terror_pos[0]][counter_terror_pos[1]] = "*"
                    defuse_command = False
                    terrorist_win = True
                    break

                elif battlefield[counter_terror_pos[0]][counter_terror_pos[1]] == "B":
                    pass
    final_print(terrorist_win, bomb_is_defused, exploded, defuse_command, bomb_pos, counter_terror_pos, seconds_left)

    battlefield[start_pos[0]][start_pos[1]] = "C"
    print(*[''.join(row) for row in battlefield], sep="\n")


n, m = map(int, input().split(", "))
counter_strike(n, m)

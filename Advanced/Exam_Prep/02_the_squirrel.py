HAZELNUTS_TO_WIN = 3

def valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size



def get_field(size):
    matrix = []
    start_position = []

    for row in range(size):
        line = [el for el in input()]
        if "s" in line:
            start_position = [row, line.index("s")]
        matrix.append(line)

    return matrix, start_position

def game(size):
    commands = input().split(", ")

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    hazelnuts = 0
    field, squirrel_pos = get_field(size)
    for direction in commands:
        r = directions[direction][0] + squirrel_pos[0]
        c = directions[direction][1] + squirrel_pos[1]

        if not valid_position(r, c, size):
            print("The squirrel is out of the field.")
            break
        squirrel_pos = [r, c]

        if field[r][c] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break

        if field[r][c] == "h":
            hazelnuts += 1
            field[r][c] = "*"

        if hazelnuts == HAZELNUTS_TO_WIN:
            print("Good job! You have collected all hazelnuts!")
            break

    else:
        print("There are more hazelnuts to collect.")

    print(f"Hazelnuts collected: {hazelnuts}")

field_size = int(input())
game(field_size)
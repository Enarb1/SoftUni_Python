SIZE = 6


def check_if_suitable(deposits_count):

    if all(d > 0 for d in deposits_count.values()):
        return "Area suitable to start the colony."
    return "Area not suitable to start the colony."


def get_position(row, col):

    if row > SIZE - 1:
        row = 0
    elif row < 0:
        row = SIZE - 1
    if col > SIZE - 1:
        col = 0
    elif col < 0:
        col = SIZE - 1

    return [row, col]


def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }


def get_matrix():
    matrix = []
    my_pos = []

    for row in range(SIZE):
        line = input().split()
        if "E" in line:
            my_pos = [row, line.index("E")]
        matrix.append(line)

    return matrix, my_pos


def martian_explorer():
    mars, rover_pos = get_matrix()
    directions = directions_mapper()
    commands = input().split(", ")

    deposits_count = {
        "W": 0,
        "M": 0,
        "C": 0
    }

    deposit_names = {
        "W": "Water",
        "M": "Metal",
        "C": "Concrete"
    }

    for direction in commands:
        r = directions[direction][0] + rover_pos[0]
        c = directions[direction][1] + rover_pos[1]

        rover_pos = get_position(r, c)

        if mars[rover_pos[0]][rover_pos[1]] == "R":
            print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
            break

        if mars[rover_pos[0]][rover_pos[1]] in deposits_count.keys():
            deposits_count[mars[rover_pos[0]][rover_pos[1]]] += 1
            dep_name = deposit_names[mars[rover_pos[0]][rover_pos[1]]]
            print(f"{dep_name} deposit found at ({rover_pos[0]}, {rover_pos[1]})")

    print(check_if_suitable(deposits_count))

martian_explorer()
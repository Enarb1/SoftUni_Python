SIZE = 6

def read_pos(matrix, my_pos):
    if matrix[my_pos[0]][my_pos[1]] != ".":
        print(matrix[my_pos[0]][my_pos[1]])

def delete_element(matrix, my_pos):
    matrix[my_pos[0]][my_pos[1]] = "."
    return matrix

def update_matrix(matrix, my_pos, actions):
    value = actions[-1]
    if matrix[my_pos[0]][my_pos[1]] != ".":
        matrix[my_pos[0]][my_pos[1]] = value
    return matrix

def create(matrix, my_pos, actions):
    value = actions[-1]
    if matrix[my_pos[0]][my_pos[1]] == ".":
        matrix[my_pos[0]][my_pos[1]] = value
    return matrix


def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }


def get_matrix():
    return [[el for el in input().split()]for row in range(SIZE)]

def crud():
    matrix = get_matrix()
    directions = directions_mapper()
    my_pos = [int(el) for el in tuple(input()) if el.isdigit()]

    actions_mapper = {
        "Create": create,
        "Update": update_matrix,
        "Delete": delete_element,
        "Read": read_pos,
    }

    while True:
        command = input()
        if command == "Stop":
            break

        actions = command.split(", ")
        direction = actions[1]
        my_pos = [my_pos[0] + directions[direction][0], my_pos[1] + directions[direction][1]]

        if len(actions) > 2:
            actions_mapper[actions[0]](matrix, my_pos,actions)
        else:
            actions_mapper[actions[0]](matrix, my_pos)

    print(*[' '.join(row) for row in matrix], sep="\n")

crud()
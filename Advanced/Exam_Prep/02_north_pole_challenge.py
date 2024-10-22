def all_items_collected(items_collected, total_items):
    return total_items == sum(items_collected.values())

def final_print(field, items_collected, names, message):
    message += "You've collected:\n"
    for items, count in items_collected.items():
       message += f"- {count} {names[items]}\n"

    message += "\n".join([' '.join(r) for r in field])

    return message

def get_position(r, c, rows, cols):

    if r > rows - 1:
        r = 0
    if r < 0:
        r = rows - 1

    if c > cols - 1:
        c = 0
    if c < 0:
        c = cols - 1

    return [r, c]


def movement(direction, steps, santa_pos, field, rows, cols, items_collected, total_items):
    directions = directions_mapper()

    while steps > 0:
        if all_items_collected(items_collected, total_items):
            break

        r = santa_pos[0] + directions[direction][0]
        c = santa_pos[1] + directions[direction][1]

        santa_pos = get_position(r, c, rows, cols)
        item = field[santa_pos[0]][santa_pos[1]]

        if item in items_collected.keys():
            items_collected[item] += 1

        field[santa_pos[0]][santa_pos[1]] = "x"
        steps -= 1

    return field, santa_pos, items_collected



def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

def get_all_items(field):
    return len([item for row in field for item in row if item != "." and item != "Y" ])

def get_matrix(rows):
    matrix = []
    santa_pos = []

    for row in range(rows):
        line = input().split()
        if "Y" in line:
            santa_pos = [row, line.index("Y")]
        matrix.append(line)

    return matrix, santa_pos


def north_pole_challenge(rows, cols):
    field, santa_pos = get_matrix(rows)
    total_items = get_all_items(field)
    field[santa_pos[0]][santa_pos[1]] = "x"


    items_collected = {
        "D": 0,
        "G": 0,
        "C": 0
    }
    names = {
        "D": "Christmas decorations",
        "G": "Gifts",
        "C": "Cookies"
    }
    message = ''

    while True:

        if all_items_collected(items_collected, total_items):
            message += "Merry Christmas!\n"
            break

        command = input()
        if command == "End":
            break

        direction, steps = command.split("-")
        steps = int(steps)
        field, santa_pos, items_collected = movement(direction, steps, santa_pos, field, rows, cols, items_collected, total_items)

    field[santa_pos[0]][santa_pos[1]] = "Y"

    return final_print(field, items_collected, names, message)

ro, co = map(int,input().split(","))
print(north_pole_challenge(ro, co))
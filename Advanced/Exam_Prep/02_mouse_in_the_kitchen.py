def check_position(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

def get_field(rows):
    matrix = []
    mouse_position = []
    cheese_count = 0

    for row in range(rows):
        line = [el for el in input()]
        if "M" in line:
            mouse_position = [row, line.index("M")]
        if "C" in line:
            cheese_count += line.count("C")
        matrix.append(line)
    matrix[mouse_position[0]][mouse_position[1]] = "*"

    return matrix, mouse_position, cheese_count


def mouse_in_kitchen(rows, cols):
    kitchen, mouse_pos, cheese = get_field(rows)

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    while True:
        command = input()
        if command == "danger":
            print("Mouse will come back later!")
            break

        direction = command
        r = mouse_pos[0] + directions[direction][0]
        c = mouse_pos[1] + directions[direction][1]

        if  not check_position(r, c, rows, cols):
            print("No more cheese for tonight!")
            break

        if kitchen[r][c] == "@":
            continue

        mouse_pos = [r, c]
        if kitchen[r][c] == "C":
            cheese -= 1
            kitchen[r][c] = "*"
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
        if kitchen[r][c] == "T":
            print("Mouse is trapped!")
            break

    kitchen[mouse_pos[0]][mouse_pos[1]] = "M"
    print(*[''.join(r) for r in kitchen], sep="\n")


size= input().split(",")
n = int(size[0])
m = int(size[1])
mouse_in_kitchen(n,m)
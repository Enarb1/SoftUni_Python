def validate_position(row, col, n, m):

    if 0 <= row < n and 0 <= col < m:
        return True
    return False


def get_matrix(rows, cols):
    delivery_boy_pos = []
    matrix = []
    for row in range(rows):
        line = [el for el in input()]
        if "B" in line:
            delivery_boy_pos = [row, line.index("B")]
        matrix.append(line)

    return matrix, delivery_boy_pos


def delivery():
    n_rows, m_cols = map(int, input().split())
    roadmap, deliveryboy_starting_pos = get_matrix(n_rows, m_cols)
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    deliveryboy_pos = deliveryboy_starting_pos
    pizza_is_picked_up = False
    delivered = False

    while not delivered:
        direction = input()
        r = deliveryboy_pos[0] + directions[direction][0]
        c = deliveryboy_pos[1] + directions[direction][1]

        if not validate_position(r, c, n_rows, m_cols):
            roadmap[deliveryboy_starting_pos[0]][deliveryboy_starting_pos[1]] = " "
            print("The delivery is late. Order is canceled.")
            break

        if not roadmap[r][c] == "*":
            deliveryboy_pos = [r, c]
            if roadmap[r][c] == "P":
                pizza_is_picked_up = True
                roadmap[r][c] = "R"
                print("Pizza is collected. 10 minutes for delivery.")
            elif pizza_is_picked_up and roadmap[r][c] == "A":
                roadmap[r][c] = "P"
                print("Pizza is delivered on time! Next order...")
                delivered = True
            else:
                if not roadmap[r][c] == "B":
                    roadmap[r][c] = "."

    print(*[''.join(row) for row in roadmap], sep='\n')

delivery()

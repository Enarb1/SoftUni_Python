CAR_MOVE = 10
TUNNEL_MOVE = 30
STARTING_POSITION = (0, 0)


def put_dot(race_track, car_position):
    race_track[car_position[0]][car_position[1]] = "."
    return race_track


def get_matrix(size):
    matrix = []
    tunnel_positions = []

    for row in range(size):
        line = input().split()
        if "T" in line:
            for i in range(len(line)):
                if line[i] == "T":
                    tunnel_positions.append((row, i))
        matrix.append(line)

    return matrix, tunnel_positions


def directions_mapper():
    return {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

def rally_racing(size, car_number):

    car_position = STARTING_POSITION
    race_track, tunnel_pos = get_matrix(size)
    directions = directions_mapper()

    kilometers = 0

    while True:
        command = input()
        if command == "End":
            print(f"Racing car {car_number} DNF.")
            break

        direction = command
        car_position = (car_position[0] + directions[direction][0], car_position[1] + directions[direction][1])

        if race_track[car_position[0]][car_position[1]] == "T":
            put_dot(race_track, car_position)
            kilometers += TUNNEL_MOVE
            tunnel_pos.remove((car_position[0], car_position[1]))
            car_position = tunnel_pos[0]
            put_dot(race_track, car_position)
            continue
        kilometers += CAR_MOVE

        if race_track[car_position[0]][car_position[1]] == "F":
            put_dot(race_track, car_position)
            print(f"Racing car {car_number} finished the stage!")
            break

    race_track[car_position[0]][car_position[1]] = "C"
    print(f"Distance covered {kilometers} km.")
    print(*[''.join(r) for r in race_track], sep="\n")


n = int(input())
racecar_number = input()

rally_racing(n, racecar_number)


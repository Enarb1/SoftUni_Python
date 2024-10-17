SUCCESSFUL_SEASON = 20


def collect_fish():
    global tons_collected
    tons_collected += int(fishing_area[my_pos[0]][my_pos[1]])


def position(row, col):
    if row < 0:
        row = size - 1
    elif row > size - 1:
        row = 0
    if col < 0:
        col = size - 1
    elif col > size - 1:
        col = 0
    return [row, col]


size = int(input())

fishing_area = []
my_pos = []

tons_collected = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = []
    for el in input():
        line.append(el)
    if "S" in line:
        my_pos = [row, line.index("S")]

    fishing_area.append(line)

fishing_area[my_pos[0]][my_pos[1]] = "-"

sink = False
while True:
    direction = input()

    if direction == "collect the nets":
        break

    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    my_pos = position(r, c)

    if fishing_area[my_pos[0]][my_pos[1]].isdigit():
        collect_fish()
        fishing_area[my_pos[0]][my_pos[1]] = "-"
    elif fishing_area[my_pos[0]][my_pos[1]] == "W":
        tons_collected = 0
        sink = True
        break

fishing_area[my_pos[0]][my_pos[1]] = "S"

if sink:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{my_pos[0]},{my_pos[1]}]")
else:
    if tons_collected >= SUCCESSFUL_SEASON:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {SUCCESSFUL_SEASON - tons_collected} tons of fish more.")
    if tons_collected > 0:
        print(f"Amount of fish caught: {tons_collected} tons.")
    print(*[''.join(row) for row in fishing_area], sep="\n")

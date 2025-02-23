def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == "V":
                nice_kids += 1

            neighborhood[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []
nice_kids_total = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    neighborhood.append(line)

    if "S" in line:
        santa_pos = [row, neighborhood[row].index("S")]
        neighborhood[santa_pos[0]][santa_pos[1]] = "-"

    nice_kids_total += neighborhood[row].count("V")

command = input()

while command != "Christmas morning":
    direction = command

    santa_pos = [
        santa_pos[0] + directions[direction][0],
        santa_pos[1] + directions[direction][1]
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1

    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or nice_kids_visited == nice_kids_total:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = "S"

if not presents and nice_kids_visited < nice_kids_total:
    print("Santa ran out of presents!")

print(*[' '.join(row) for row in neighborhood], sep='\n')

if nice_kids_visited == nice_kids_total:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_total - nice_kids_visited} nice kid/s.")
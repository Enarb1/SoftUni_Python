def find_all_paths(row, col, lab, moves, max_moves, found_exit):

    if row >= len(lab) or row < 0 or col >= len(lab[0]) or col < 0:
        max_moves[0] = max(max_moves[0], moves)
        found_exit[0] = True
        return 0

    if lab[row][col] == "#" or lab[row][col] == "v":
       return 0

    lab[row][col] = 'v'
    moves += find_all_paths(row, col + 1, lab, moves + 1, max_moves, found_exit) #right
    moves +=find_all_paths(row, col - 1, lab,moves + 1, max_moves, found_exit) #left
    moves +=find_all_paths(row - 1, col, lab, moves + 1, max_moves, found_exit) #up
    moves +=find_all_paths(row + 1, col, lab, moves + 1, max_moves, found_exit) #down
    lab[row][col] = ' '

    return 0


rows = int(input())

lab = []
kate_pos = None

for row in range(rows):
    line = list(input())
    if "k" in line:
        kate_pos = (row, line.index("k"))
    lab.append(line)

max_moves = [0]
found_exit = [False]
find_all_paths(kate_pos[0], kate_pos[1], lab, 0, max_moves, found_exit)

if found_exit[0]:
    print(f"Kate got out in {max_moves[0]} moves")
else:
    print("Kate cannot get out")
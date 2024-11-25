def find_shortest_path(row, col, lab,moves,min_moves, size):

    if row < 0:
        row = row + 1

    if col < 0:
        col = col + 1

    if row >= size:
        row = size - 1

    if col >= size:
        col = col - 1

    if lab[row][col] == "E":
        min_moves[0] = min(min_moves[0],moves)
        return 0

    if lab[row][col] == 'v' or lab[row][col] == '#':
        return 0

    lab[row][col] = "v"

    moves += find_shortest_path(row, col + 1, lab, moves + 1,min_moves, size)  # right
    moves += find_shortest_path(row, col - 1, lab, moves + 1,min_moves, size)  # left
    moves += find_shortest_path(row - 1, col, lab, moves + 1,min_moves, size)  # up
    moves += find_shortest_path(row + 1, col, lab, moves + 1,min_moves, size)  # down
    lab[row][col] = ' '

    return 0


n = int(input())
matrix = [[l for l in list(input())]for r in range(n)]


min_moves = [float('inf')]
find_shortest_path(0, 0, matrix,0,min_moves, n)
print(min_moves[0])

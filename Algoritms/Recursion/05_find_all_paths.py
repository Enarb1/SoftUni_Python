def is_invalid(row, col , lab):
    return row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0])

def find_paths(row, col, direction, lab, paths):
    if is_invalid(row, col, lab):
        return

    if lab[row][col] == '*':
        return

    if lab[row][col] == 'v':
        return

    paths.append(direction)

    if lab[row][col] == 'e':
        print(''.join(paths))
    else:
        lab[row][col] = 'v'
        find_paths(row, col + 1, "R", lab, paths)
        find_paths(row, col - 1, "L", lab, paths)
        find_paths(row - 1, col, "U", lab, paths)
        find_paths(row + 1, col, "D", lab, paths)
        lab[row][col] = '-'

    paths.pop()


rows = int(input())
cols = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))

find_paths(0, 0, '', lab, [])
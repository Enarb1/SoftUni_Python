n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in c.split(","))for c in input().split())

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, 1),
    (-1, -1),
    (1, 1),
    (1, -1),
    (0, 0)
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:

        r_exp, c_exp = row + x, col + y

        if 0 <= r_exp < n and 0 <= c_exp < n:
            matrix[r_exp][c_exp] -= matrix[row][col] if matrix[r_exp][c_exp] > 0 else 0


alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]



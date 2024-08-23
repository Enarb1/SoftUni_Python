n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = ((int(x) for x in c.split(","))for c in input().split())


for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    bomb_value = matrix[row][col]

    for x in range(-1, 2):  # In order to not use directions variable, this guaranties that we loop through
        # all possible directions
        for y in range(-1, 2):
            r_exp, c_exp = row + x, col + y

            if 0 <= r_exp < n and 0 <= c_exp < n:
                matrix[r_exp][c_exp] -= bomb_value if matrix[r_exp][c_exp] > 0 else 0


alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]



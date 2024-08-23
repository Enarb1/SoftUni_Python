n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break

    order, row, col, value = command.split()

    if 0 <= int(row) < n and 0 <= int(col) < n:
        if order == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif order == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")

[print(*row) for row in matrix]
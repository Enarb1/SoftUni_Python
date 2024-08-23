n = int(input())

matrix = []

for row in range(n):
    row_data = [el for el in input()]
    matrix.append(row_data)

wanted_symbol = input()
position = None

for row_index in range(len(matrix)):
    if position is not None:
        break
    for col_index in range(len(matrix)):
        if matrix[row_index][col_index] == wanted_symbol:
            position = (row_index, col_index)
            print(position)
            break

if position is None:
    print(f"{wanted_symbol} does not occur in the matrix")


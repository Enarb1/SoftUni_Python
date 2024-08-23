def validate_indices(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


"""If we want to use an if statement and not a set"""


# if 0 <= indices[0] < rows and 0 <= indices[2] < rows and 0 <= indices[1] < cols and 0 <= indices[3] < cols:
#     return True
# return False

def swap_indices(command, indices):
    if len(indices) == 4 and validate_indices(indices) and command == 'swap':
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_indices(command_type, coordinates)

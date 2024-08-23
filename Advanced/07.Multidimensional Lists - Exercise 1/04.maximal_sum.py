rows, columns = map(int, input().split())

matrix = [[int(el) for el in input().split()] for row in range(rows)]

max_sum = float('-inf')
sub_matrix = []
for row_i in range(rows - 2):
    for col_i in range(columns - 2):
        first_row = matrix[row_i][col_i:col_i + 3]
        second_row = matrix[row_i + 1][col_i:col_i + 3]
        third_row = matrix[row_i + 2][col_i:col_i + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]

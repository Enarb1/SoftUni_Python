rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

max_sum = float('-inf')
sub_matrix = None
for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        main_el = matrix[row_index][col_index]
        right_el = matrix[row_index][col_index + 1]
        down_el = matrix[row_index + 1][col_index]
        down_right_el = matrix[row_index + 1][col_index + 1]
        current_sum = sum((main_el, right_el,down_el, down_right_el))

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[main_el, right_el], [down_el, down_right_el]]

if sub_matrix:
    print(*sub_matrix[0], sep=' ')
    print(*sub_matrix[1], sep=' ')
print(max_sum)

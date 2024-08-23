rows, column = [int(el) for el in input().split(", ")]

matrix = []
for row in range(rows):
    rows_nums = [int(el) for el in input().split()]
    matrix.append(rows_nums)

for col_index in range(column):
    sum_nums = 0
    for row_index in range(rows):
        sum_nums += matrix[row_index][col_index]
    print(sum_nums)



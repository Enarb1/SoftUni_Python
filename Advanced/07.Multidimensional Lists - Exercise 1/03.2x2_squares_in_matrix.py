"""My solution"""


rows, columns = map(int, input().split())

matrix = [[el for el in input().split()]for row in range(rows)]

same_count = 0

for row_i in range(rows -1):
    for col_i in range(columns -1):
        main_el = matrix[row_i][col_i]
        right_el = matrix[row_i][col_i + 1]
        down_el = matrix[row_i + 1][col_i]
        down_right_el = matrix[row_i + 1][col_i + 1]
        sub_list = [main_el, right_el, down_el,down_right_el]
        if all(el == main_el for el in sub_list):
            same_count += 1

print(same_count)


"""Solution from the exercise"""

rows, columns = map(int, input().split())
matrix = [[el for el in input().split()]for row in range(rows)]

same_count = 0

for row_i in range(rows - 1):
    for col_i in range(columns - 1):
        element = matrix[row_i][col_i]

        if (element == matrix[row_i][col_i + 1] and element == matrix[row_i + 1][col_i] and
                element == matrix[row_i + 1][col_i + 1]):
            same_count += 1

print(same_count)

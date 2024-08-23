rows = int(input())

matrix = []

# for row in range(rows):
#     nums_row = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
#     matrix.append(nums_row)
#
# print(matrix)

for row in range(rows):
    row_data = input().split(', ')
    row_nums = []
    for el in row_data:
        if int(el) % 2 == 0:
            row_nums.append(int(el))
    matrix.append(row_nums)

print(matrix)

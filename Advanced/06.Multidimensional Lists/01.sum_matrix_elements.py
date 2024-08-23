rows, columns = [int(el) for el in input().split(', ')]

matrix = []
sum_nums = 0

for i in range(rows):
    row_nums = [int(num) for num in input().split(", ")]
    sum_nums += sum(row_nums)
    matrix.append(row_nums)

print(sum_nums)
print(matrix)

""""Longer version with unnecessary second loop"""

# for row in range(rows):
#     row_data = input().split(', ')
#     row_numbers = []
#     for index in range(len(row_data)):
#         current_el = int(row_data[index])
#         sum_nums += current_el
#         row_numbers.append(current_el)
#     matrix.append(row_numbers)
#
# print(sum_nums)
# print(matrix)

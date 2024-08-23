n = int(input())

matrix = []

for row in range(n):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

diagonal_sum = 0

for index in range(n):
    diagonal_sum += matrix[index][index]

# for row_i in range(n):
#     for col_i in range(n):
#         if col_i == row_i:
#             diagonal_sum += matrix[row_i][col_i]

print(diagonal_sum)

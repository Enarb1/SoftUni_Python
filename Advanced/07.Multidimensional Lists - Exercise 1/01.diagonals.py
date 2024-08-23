n = int(input())
matrix = [[col for col in map(int, input().split(", "))]for row in range(n)]


primary_diagonal = []

for index in range(n):
    primary_diagonal.append(matrix[index][index])

secondary_diagonal = []
row_i = 0
for col_index in range(len(matrix) - 1, -1, -1):
    secondary_diagonal.append(matrix[row_i][col_index])
    row_i += 1


print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}\n"
      f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

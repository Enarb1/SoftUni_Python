n = int(input())

matrix = [[col for col in map(int, input().split(", "))]for _ in range(n)]
primary = [matrix[index][index] for index in range(n)]
secondary = [matrix[row][n - row - 1] for row in range(n)]

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}\n"
      f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")
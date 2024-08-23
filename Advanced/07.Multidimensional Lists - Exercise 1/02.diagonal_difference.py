""""My VAR , but it has too many loops"""

n = int(input())

matrix = [[int(el) for el in input().split()]for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

diff = abs(sum(primary) - sum(secondary))

print(diff)

""""First Var from video"""

n = int(input())

matrix = [[int(el) for el in input().split()]for _ in range(n)]
primary_sum, secondary_sum = 0, 0

for i in range(n):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][n - i - 1]

print(abs(primary_sum - secondary_sum))

""""Faster solution without even making a matrix"""

n = int(input())
primary_sum, secondary_sum = 0, 0

for i in range(n):
    line = [int(x) for x in input().split()]
    primary_sum += line[i]
    secondary_sum += line[n - i - 1]

print(abs(primary_sum - secondary_sum))

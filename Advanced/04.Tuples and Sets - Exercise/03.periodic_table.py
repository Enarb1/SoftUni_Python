n = int(input())
result = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        result.add(el)

print(*result, sep='\n')
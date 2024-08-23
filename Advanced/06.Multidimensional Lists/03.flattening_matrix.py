rows = int(input())

flattened = []

for row in range(rows):
    row_nums = [int(el) for el in input().split(", ")]
    flattened.extend(row_nums)


print(flattened)

# matrix = [map(int,input().split(", ")) for _ in range(int(input()))]
# flattened = [num for row in matrix for num in row]
# print(flattened)
number_of_lines = int(input())
capacity = 255

for line in range(number_of_lines):
    water = int(input())
    if capacity - water < 0:
        print("Insufficient capacity!")
        continue
    capacity -= water
print(255 - capacity)

numbers_input = input().split()
numbers_int = []

for num in numbers_input:
    numbers_int.append(int(num))

result = filter(lambda numb: numb % 2 == 0, numbers_int)

print(list(result))





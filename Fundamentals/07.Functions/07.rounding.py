input_string = input().split()
numbers_list = []

for num in input_string:
    numbers_list.append(round(float(num)))


print(numbers_list)
input_list = input().split(", ")
list_of_numbers = []
list_of_zeroes = []

for number in input_list:
    list_of_numbers.append(int(number))

for num in reversed(list_of_numbers):
    if int(num) == 0:
        list_of_numbers.remove(num)
        list_of_zeroes.append(int(num))

for zero in list_of_zeroes:
    list_of_numbers.append(zero)
print(list_of_numbers)


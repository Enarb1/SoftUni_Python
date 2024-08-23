factor_number = int(input())
list_lenght = int(input())
list_of_numbers = []
last_number = 0
while len(list_of_numbers) < list_lenght:
    last_number += factor_number
    list_of_numbers.append(last_number)
print(list_of_numbers)


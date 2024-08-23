input_string = input()
numbers_to_remove = int(input())
numbers_list = input_string.split(" ")
numbers_list_int = []

for string in numbers_list:
    numbers_list_int.append(int(string))

temp_list = []
for number in numbers_list_int:
    temp_list.append(number)

temp_list.sort()
temp_list = temp_list[numbers_to_remove:]
final_list = []
for element in numbers_list_int:
    if element in temp_list:
        final_list.append(element)
print(", ".join(map(str,final_list)))








input_of_numbers = input()
string_number_list = input_of_numbers.split(" ")
int_number_list = []
inverted_number_list = []

for string in string_number_list:
    int_number_list.append(int(string))
for number in int_number_list:
    if number > 0:
        number = -number
    elif number < 0:
        number = number - number - number
    inverted_number_list.append(number)
print(inverted_number_list)






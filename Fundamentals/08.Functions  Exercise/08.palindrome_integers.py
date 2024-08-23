
def rev(list_of_numbers):
    list_to_reverse = list_of_numbers
    reversed_nums = []

    for num_str in list_of_numbers:
        reversed_nums.append(num_str[::-1])

    return reversed_nums


input_list = input().split(", ")
rev_list = rev(input_list)

for index in range(len(input_list)):
    if input_list[index] == rev_list[index]:
        print(True)
    else:
        print(False)


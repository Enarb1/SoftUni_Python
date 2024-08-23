
def sorted_numbers(numbers):
    input_string = numbers
    int_list = []
    for num in input_string:
        int_list.append(int(num))

    return sorted(int_list)


input_nums = input().split()
print(sorted_numbers(input_nums))

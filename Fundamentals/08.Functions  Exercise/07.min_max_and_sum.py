
def min_number(number):
    numbs_as_string = number
    numbers_list = []
    for num in numbs_as_string:
        numbers_list.append(int(num))
    return min(numbers_list)


def max_number(number):
    number_as_string = number
    numbers_list = []
    for num in number_as_string:
        numbers_list.append(int(num))
    return max(numbers_list)


def sum_numbs(number):
    number_as_string = number
    total = 0
    for num in number_as_string:
        total += int(num)
    return total


input_string = input().split()
print(f"The minimum number is {min_number(input_string)}")
print(f"The maximum number is {max_number(input_string)}")
print(f"The sum number is: {sum_numbs(input_string)}")
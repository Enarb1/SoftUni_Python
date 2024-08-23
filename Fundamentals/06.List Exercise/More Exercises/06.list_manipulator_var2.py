from itertools import islice


def exchange(first_list, command, index):

    left = first_list[index + 1:]
    right = first_list[:index + 1]
    first_list = []
    first_list.extend(left)
    first_list.extend(right)

    return first_list


def max_even(first_list):

    max_even_index = "No matches"
    max_even_num = float('-inf')
    for index, num in enumerate(first_list):
        if int(num) % 2 == 0:
            if int(num) >= max_even_num:
                max_even_num = int(num)
                max_even_index = index

    return max_even_index


def max_odd(first_list):
    max_odd_index = "No matches"
    max_odd_num = float('-inf')
    for index, num in enumerate(first_list):
        if int(num) % 2 != 0:
            if int(num) >= max_odd_num:
                max_odd_num = int(num)
                max_odd_index = index

    return max_odd_index


def min_even(first_list):
    min_even_index = "No matches"
    min_even_num = float('inf')
    for index, num in enumerate(first_list):
        if int(num) % 2 == 0:
            if int(num) <= min_even_num:
                min_even_num = int(num)
                min_even_index = index

    return min_even_index


def min_odd(first_list):
    min_odd_index = "No matches"
    min_odd_num = float('inf')
    for index, num in enumerate(first_list):
        if int(num) % 2 != 0:
            if int(num) <= min_odd_num:
                min_odd_num = int(num)
                min_odd_index = index

    return min_odd_index


def first_count_even(first_list,num_count):

    even_nums = list(islice((num for num in first_list if int(num) % 2 == 0), num_count))
    return list(map(int, even_nums)) if even_nums else []


def first_count_odd(first_list,num_count):

    odd_nums = list(islice((num for num in first_list if int(num) % 2 != 0), num_count))
    return list(map(int, odd_nums)) if odd_nums else []


def last_count_even(first_list,num_count):
    last_even = []
    for num in first_list:
        if int(num) % 2 == 0:
            last_even.append(num)
            if len(last_even) > num_count:
                last_even.pop(0)
    return list(map(int, last_even))


def last_count_odd(first_list,num_count):
    last_odd = []
    for num in first_list:
        if int(num) % 2 != 0:
            last_odd.append(num)
            if len(last_odd) > num_count:
                last_odd.pop(0)
    return list(map(int, last_odd))


input_list = input().split()

while True:
    command = input()
    if command == 'end':
        break
    command_list = command.split()
    if command_list[0] == 'exchange':
        if int(command_list[1]) >= len(input_list) or int(command_list[1]) < 0:
            print("Invalid index")
        else:
            input_list = exchange(input_list, command_list[0], int(command_list[1]))
    elif command_list[0] == "max":
        if command_list[1] == 'even':
            print(max_even(input_list))
        elif command_list[1] == 'odd':
            max_index_odd = max_odd(input_list)
            print(max_index_odd)
    elif command_list[0] == 'min':
        if command_list[1] == 'even':
            print(min_even(input_list))
        elif command_list[1] == 'odd':
            print(min_odd(input_list))
    elif command_list[0] == "first":
        count = int(command_list[1])
        if count > len(input_list):
            print("Invalid count")
        else:
            if command_list[2] == 'even':
                print(first_count_even(input_list, count))
            elif command_list[2] == 'odd':
                print(first_count_odd(input_list, count))
    elif command_list[0] == 'last':
        count = int(command_list[1])
        if count > len(input_list):
            print("Invalid count")
        else:
            if command_list[2] == 'even':
                print(last_count_even(input_list, count))
            elif command_list[2] == "odd":
                print(last_count_odd(input_list, count))
print(list(map(int, input_list)))
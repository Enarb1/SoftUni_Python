def swap_elements(array_lst, idx1, idx2):

    array_lst[idx1], array_lst[idx2] = array_lst[idx2], array_lst[idx1]


def multiply(array_lst, idx1, idx2):

    new_element = array_lst[idx1] * array_lst[idx2]
    array_lst.pop(idx1)
    array_lst.insert(idx1, new_element)


def decrease(array_lst):

    new_lst = [num - 1 for num in array_lst]
    array_lst = new_lst

    return array_lst


def process_command(array_list, commands):
    for command in commands:
        command_list = command.split()
        if command_list[0] == 'swap':
            index_one = int(command_list[1])
            index_two = int(command_list[2])
            swap_elements(array_list, index_one, index_two)
        elif command_list[0] == 'multiply':
            index_one = int(command_list[1])
            index_two = int(command_list[2])
            multiply(array_list, index_one, index_two)
        elif command_list[0] == 'decrease':
            array_list = decrease(array_list)

    return array_list


array_input = list(map(int,input().split()))
commands = []
while True:
    command_input = input()
    if command_input == 'end':
        break
    commands.append(command_input)


result = ", ".join(list(map(str,process_command(array_input,commands))))
print(result)




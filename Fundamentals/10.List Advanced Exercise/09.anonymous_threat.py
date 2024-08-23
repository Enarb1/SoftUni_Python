def merge(initial_list, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(initial_list) - 1, end_index)

    if start_index < end_index:
        merged = ''.join(initial_list[start_index:end_index + 1])
        initial_list[start_index:end_index + 1] = [merged]


def divide(initial_list, index, partitions):
    element = initial_list[index]
    part_length = len(element) // partitions

    divided_parts = []
    start = 0

    for i in range(partitions):
        if i == partitions - 1:
            divided_parts.append(element[start:])
        else:
            divided_parts.append(element[start:start + part_length])
            start += part_length

    initial_list[index:index + 1] = divided_parts


def process_commands(initial_list, commands_list):
    for command in commands_list:
        parts = command.split()

        if parts[0] == 'merge':
            start_index = int(parts[1])
            end_index = int(parts[2])
            merge(initial_list,start_index,end_index)
        elif parts[0] == 'divide':
            index = int(parts[1])
            partitions = int(parts[2])
            divide(initial_list, index, partitions)

    return initial_list


initial_list = input().split()
commands = []

while True:
    command = input()

    if command == '3:1':
        break

    commands.append(command)

result = process_commands(initial_list, commands)
print(" ".join(result))


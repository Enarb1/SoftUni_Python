def urgent(shopping_list, item):
    if item not in shopping_list:
        shopping_list.insert(0, item)


def unnecessary(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)


def correct(shopping_list, old_item, new_item):
    for index, item in enumerate(shopping_list):
        if item == old_item:
            shopping_list.pop(index)
            shopping_list.insert(index, new_item)


def rearrange(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)


def process_commands(shopping_list, commands_list):

    for comm in commands_list:
        command_parts = comm.split()
        if command_parts[0] == "Urgent":
            item = command_parts[1]
            urgent(shopping_list, item)
        elif command_parts[0] == "Unnecessary":
            item = command_parts[1]
            unnecessary(shopping_list, item)
        elif command_parts[0] == "Correct":
            old_item = command_parts[1]
            new_item = command_parts[2]
            correct(shopping_list, old_item, new_item)
        elif command_parts[0] == "Rearrange":
            item = command_parts[1]
            rearrange(shopping_list, item)

    return ", ".join(shopping_list)


initial_shopping_lst = input().split("!")
commands = []

while True:
    command = input()
    if command == "Go Shopping!":
        break
    commands.append(command)

print(process_commands(initial_shopping_lst, commands))
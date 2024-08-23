def collect(items_lst, item):
    if item not in items_lst:
        items_lst.append(item)

def drop(items_lst, item):
    if item in items_lst:
        items_lst.remove(item)

def combine(items_lst, items):
    old_new = items.split(":")
    old_item = old_new[0]
    new_item = old_new[1]
    if old_item in items_lst:
        for index, item in enumerate(items_lst):
            if item == old_item:
                if index + 1 < len(items_lst):
                    items_lst.insert(index + 1, new_item)
                else:
                    items_lst.append(new_item)


def renew(items_lst, item):
    if item in items_lst:
        items_lst.remove(item)
        items_lst.append(item)


def process_command(items_lst, commands_lst):
    for com in commands_lst:
        command_parts = com.split(" - ")
        if command_parts[0] == "Collect":
            item = command_parts[1]
            collect(items_lst, item)
        elif command_parts[0] == "Drop":
            item = command_parts[1]
            drop(items_lst, item)
        elif command_parts[0] == "Combine Items":
            items = command_parts[1]
            combine(items_lst, items)
        elif command_parts[0] == "Renew":
            item = command_parts[1]
            renew(items_lst, item)
    return ", ".join(items_lst)


initial_items_list = input().split(", ")
commands = []

while True:
    command = input()
    if command == "Craft!":
        break
    commands.append(command)


print(process_command(initial_items_list,commands))
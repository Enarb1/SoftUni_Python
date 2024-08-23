def loot(treasure_chest, items):
    items_lst = items[1:]
    for item in items_lst:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)


def drop(treasure_chest, index):
    if 0 <= index < len(treasure_chest):
        for idx, loot_item in enumerate(treasure_chest):
            if idx == index:
                new_item = loot_item
                treasure_chest.pop(index)
                treasure_chest.append(new_item)


def steal(treasure_chest, count):
    if count > len(treasure_chest):
        stolen = treasure_chest[:]
        treasure_chest = []
    else:
        stolen = treasure_chest[len(treasure_chest) - count:]
        treasure_chest = treasure_chest[:len(treasure_chest) - count]
    print(", ".join(stolen))
    return treasure_chest


def process_command(treasure_chest, commands):
    for command in commands:
        command_parts = command.split()
        if command_parts[0] == "Loot":
            loot(treasure_chest,command_parts)
        elif command_parts[0] == "Drop":
            index = int(command_parts[1])
            drop(treasure_chest, index)
        elif command_parts[0] == "Steal":
            count = int(command_parts[1])
            treasure_chest = steal(treasure_chest, count)
    return treasure_chest


initial_treasure_chest = input().split("|")
commands_list = []

while True:
    command_input = input()
    if command_input == "Yohoho!":
        break
    commands_list.append(command_input)

treasure = process_command(initial_treasure_chest,commands_list)
word_sum = 0
if len(treasure) == 0:
    print("Failed treasure hunt.")
else:
    for word in treasure:
        word_sum += len(word)
    average = word_sum / len(treasure)
    print(f"Average treasure gain: {average:.2f} pirate credits.")


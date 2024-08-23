def shoot(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add(targets, index, value):

    if index > len(targets) or index < 0:
        print("Invalid placement!")
    else:
        targets.insert(index, value)


def strike(targets, index, radius):
        indexes_valid = False
        if 0 <= index + radius < len(targets) and 0 <= index - radius < len(targets):
            indexes_valid = True
        if indexes_valid:
            map(str, targets)
            targets = targets[:index - radius] + targets[(index + 1) + radius:]
            map(int, targets)
        else:
            print("Strike missed!")
        return targets


def process_commands(targets, shot_commands):
    for command in shot_commands:
        command_lst = command.split()

        if command_lst[0] == "Shoot":
            index = int(command_lst[1])
            power = int(command_lst[2])
            shoot(targets, index, power)
        elif command_lst[0] == "Add":
            index = int(command_lst[1])
            value = int(command_lst[2])
            add(targets, index, value)
        elif command_lst[0] == "Strike":
            index = int(command_lst[1])
            radius = int(command_lst[2])
            targets = strike(targets, index, radius)
    return targets


sequence_of_targets = list(map(int,input().split()))
shots_list = []
while True:
    cmnd = input()
    if cmnd == "End":
        break
    shots_list.append(cmnd)

print("|".join(map(str, process_commands(sequence_of_targets, shots_list))))
def cupid_jump(houses_lst, commands_lst):
    house_index = 0

    for command in commands_lst:
        commands_parts = command.split()
        jump_index = int(commands_parts[1])
        index = jump_index + house_index
        if index > len(houses_lst) -1:
            index = 0
            house_index = index
        if houses_lst[index] == 0:
            print(f"Place {index} already had Valentine's day.")
        else:
            houses_lst[index] = houses_lst[index] - 2
            house_index = index
            if houses_lst[index] == 0:
                print(f"Place {index} has Valentine's day." )
    print(f"Cupid's last position was {house_index}.")
    if sum(houses_lst) == 0:
        print("Mission was successful.")
    else:
        house_left = [num for num in houses_lst if num > 0]
        print(f"Cupid has failed {len(house_left)} places.")


houses_list = list(map(int, input().split("@")))
commands = []
while True:
    command = input()
    if command == "Love!":
        break
    commands.append(command)

cupid_jump(houses_list, commands)

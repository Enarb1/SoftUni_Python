gifts_planned_to_buy = input().split(" ")
command = input()

while command != "No Money":
    commands_list = command.split(" ")
    if commands_list[0] == "OutOfStock":
        for index in range(len(gifts_planned_to_buy)-1,-1,-1):
            if commands_list[1] == gifts_planned_to_buy[index]:
                gifts_planned_to_buy[index] = "None"
    elif commands_list[0] == "Required":
        for index in range(len(gifts_planned_to_buy)):
            if index == int(commands_list[2]):
                gifts_planned_to_buy[int(commands_list[2])] = commands_list[1]
    elif commands_list[0] == "JustInCase":
        gifts_planned_to_buy[-1] = commands_list[1]
    command = input()
for index in range(len(gifts_planned_to_buy)):
    if gifts_planned_to_buy[index] == 'None':
        continue
    print(gifts_planned_to_buy[index], end=' ')

def status(pirate_ship, max_health):
    count = 0
    for section in pirate_ship:
        if section < (0.2 * max_health):
            count += 1
    print(f"{count} sections need repair.")


def repair(pirate_ship, max_health, index, health):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health


def defend(pirate_ship, warship, start_index, end_index, damage):
    if 0 <= start_index < len(pirate_ship) and start_index <= end_index < len(pirate_ship):
        for idx, hit in enumerate(pirate_ship):
            if start_index <= idx <= end_index:
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    return True
    return False


def fire(pirate_ship, warship,index, damage):
    if 0 <= index < len(warship):
        warship[index] = warship[index] - damage
        if warship[index] <= 0:
            return True
    return False


def process_commands(pirate_ship, warship, commands, max_health):
    for command in commands:
        command_part = command.split()
        if command_part[0] == "Fire":
            index = int(command_part[1])
            damage = int(command_part[2])
            if fire(pirate_ship, warship, index, damage):
                return "You won! The enemy ship has sunken."
        elif command_part[0] == "Defend":
            start_index = int(command_part[1])
            end_index = int(command_part[2])
            damage = int(command_part[3])
            if defend(pirate_ship,warship,start_index,end_index,damage):
                return "You lost! The pirate ship has sunken."
        elif command_part[0] == "Repair":
            index = int(command_part[1])
            health = int(command_part[2])
            repair(pirate_ship,max_health,index,health)
        elif command_part[0] == "Status":
            status(pirate_ship, max_health)

    return f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}"


pirate_ship_input = list(map(int, input().split(">")))
warship_input = list(map(int,input().split(">")))
max_health_input = int(input())
commands_input = []

while True:
    cmnd = input()
    if cmnd == "Retire":
        break
    commands_input.append(cmnd)
print(process_commands(pirate_ship_input, warship_input, commands_input, max_health_input))
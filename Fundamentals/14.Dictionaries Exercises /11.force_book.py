def line(force_sides, side, user):

    if side not in force_sides.keys() and user not in (usr for users in force_sides.values()for usr in users):
        force_sides[side] = []
        force_sides[side].append(user)
    elif not any(user in users for users in force_sides.values()):
        force_sides[side].append(user)


def arrow(force_sides, side, user):

    if side not in force_sides.keys():
        force_sides[side] = []
        for force, value in force_sides.items():
            if user in value:
                force_sides[force].remove(user)
        if user not in force_sides.items():
            force_sides[side].append(user)
    elif not any(user in users for users in force_sides.values()):
        force_sides[side].append(user)
    else:
        for force_side, value in force_sides.items():
            if user in value:
                force_sides[force_side].remove(user)
                force_sides[side].append(user)
    print(f"{user} joins the {side} side!")


sides = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if "|" in command:
        input_line = command.split(" | ")
        side = input_line[0]
        user = input_line[1]
        line(sides, side, user)
    elif "->" in command:
        input_line = command.split(" -> ")
        user = input_line[0]
        side = input_line[1]
        arrow(sides, side, user)

for side, name in sides.items():
    if len(name) > 0:
        print(f"Side: {side}, Members: {len(name)}")
        for user in name:
            print(f'! {user}')
        #print(f'! {"\n! ".join(user for user in name)}')
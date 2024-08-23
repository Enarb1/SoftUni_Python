def plunder(targets, town, people, gold):

    targets[town]['population'] -= people
    targets[town]['gold'] -= gold
    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    if targets[town]['population'] <= 0 or targets[town]['gold'] <= 0:
        print(f'{town} has been wiped off the map!')
        del targets[town]

    return targets


def prosper(targets, town, gold):

    if gold < 0:
        print(f'Gold added cannot be a negative number!')
    else:
        targets[town]['gold'] += gold
        total_gold = targets[town]['gold']
        print(f'{gold} gold added to the city treasury. {town} now has {total_gold} gold.')
    return targets


def process_commands(targets):

    while True:
        command = input()
        if command == 'End':
            break
        line_input = command.split('=>')
        action = line_input[0]
        town = line_input[1]
        if action == 'Plunder':
            people = int(line_input[2])
            gold = int(line_input[3])
            targets = plunder(targets, town, people, gold)
        elif action == 'Prosper':
            gold = int(line_input[2])
            targets = prosper(targets, town, gold)

    if len(targets) > 0:
        print(f'Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:')
        for town in targets.keys():
            people = targets[town]['population']
            gold = targets[town]['gold']
            print(f'{town} -> Population: {people} citizens, Gold: {gold} kg')
    else:
        print('Ahoy, Captain! All targets have been plundered and destroyed!')


def add_targets(targets):

    while True:
        command = input()
        if command == 'Sail':
            break
        target_info = command.split("||")
        town = target_info[0]
        people = int(target_info[1])
        gold = int(target_info[2])
        if town not in targets.keys():
            targets[town] = {'population': 0, 'gold': 0}
        targets[town]['population'] += people
        targets[town]['gold'] += gold

    return targets


target_towns = {}
target_towns = add_targets(target_towns)
process_commands(target_towns)
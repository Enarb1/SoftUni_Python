def alteration_func(spell, sub):
    if sub in spell:
        spell = spell.replace(sub, '')
        print(spell)
    return spell


def divination_func(spell, first_sub, second_sub):
    if first_sub in spell:
        spell = spell.replace(first_sub, second_sub)
        print(spell)
    return spell


def necromancy_func(spell):
    spell = spell.lower()
    print(spell)
    return spell


def abjuration_func(spell):
    spell = spell.upper()
    print(spell)
    return spell


def illusion_func(spell, index, letter):
    if index < 0 or index >= len(spell):
        print('The spell was too weak.')
    else:
        spell = spell.replace(spell[index], letter, 1)
        print('Done!')
    return spell


def process_commands(spell):
    while True:
        command = input()
        if command == 'Abracadabra':
            break
        info = command.split()
        action = info[0]
        if action == 'Abjuration':
            spell = abjuration_func(spell)
        elif action == 'Necromancy':
            spell = necromancy_func(spell)
        elif action == 'Illusion':
            index = int(info[1])
            letter = info[2]
            spell = illusion_func(spell, index, letter)
        elif action == "Divination":
            first_substring = info[1]
            second_substring = info[2]
            spell = divination_func(spell, first_substring, second_substring)
        elif action == 'Alteration':
            substring = info[1]
            spell = alteration_func(spell, substring)
        else:
            print('The spell did not work!')


initial_spell = input()
process_commands(initial_spell)

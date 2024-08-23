def cast_spell(heroes, hero, mp_needed, spell):

    if heroes[hero]['MP'] >= mp_needed:
        heroes[hero]['MP'] -= mp_needed
        current_mp = heroes[hero]['MP']
        print(f'{hero} has successfully cast {spell} and now has {current_mp} MP!')
    else:
        print(f'{hero} does not have enough MP to cast {spell}!')

    return heroes


def take_damage(heroes, hero, damage, attacker):

    heroes[hero]['HP'] -= damage
    if heroes[hero]['HP'] <= 0:
        print(f'{hero} has been killed by {attacker}!')
        del heroes[hero]
    else:
        current_hp = heroes[hero]['HP']
        print(f'{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')

    return heroes


def recharge(heroes, hero, mp_amount, MAX_MP):

    if heroes[hero]['MP'] + mp_amount > MAX_MP:
        amount_recovered = MAX_MP - heroes[hero]['MP']
    else:
        amount_recovered = mp_amount

    heroes[hero]['MP'] += mp_amount
    if heroes[hero]['MP'] > MAX_MP:
        heroes[hero]['MP'] = MAX_MP
    print(f'{hero} recharged for {amount_recovered} MP!')

    return heroes


def heal(heroes, hero, hp_amount, MAX_HP):

    if heroes[hero]['HP'] + hp_amount > MAX_HP:
        amount_recovered = MAX_HP - heroes[hero]['HP']
    else:
        amount_recovered = hp_amount

    heroes[hero]['HP'] += hp_amount
    if heroes[hero]['HP'] > MAX_HP:
        heroes[hero]['HP'] = MAX_HP
    print(f'{hero} healed for {amount_recovered} HP!')

    return heroes


def add_heroes(loop_range, heroes, MAX_HP , MAX_MP):

    for _ in range(loop_range):
        hero, hp, mp = input().split()
        if int(hp) > MAX_HP:
            hp = MAX_HP
        if int(mp) > MAX_MP:
            mp = MAX_MP
        if hero not in heroes.keys():
            heroes[hero] = {}
        heroes[hero] = {'HP': int(hp), 'MP': int(mp)}
    return heroes


def process_commands(MAX_HP, MAX_MP, heroes_lst):
    while True:
        command = input()
        if command == 'End':
            break

        line_input = command.split(" - ")
        action = line_input[0]
        hero_name = line_input[1]

        if action == 'CastSpell':
            mp_needed = int(line_input[2])
            spell_name = line_input[3]
            heroes_lst = cast_spell(heroes_lst, hero_name, mp_needed, spell_name)
        elif action == 'TakeDamage':
            damage = int(line_input[2])
            attacker_name = line_input[3]
            heroes_lst = take_damage(heroes_lst, hero_name, damage, attacker_name)
        elif action == 'Recharge':
            amount = int(line_input[2])
            heroes_lst = recharge(heroes_lst, hero_name, amount, MAX_MP)
        elif action == 'Heal':
            amount = int(line_input[2])
            heroes_lst = heal(heroes_lst, hero_name, amount, MAX_HP)

    for hero in heroes_lst.keys():
        current_hp = heroes_lst[hero]['HP']
        current_mp = heroes_lst[hero]['MP']
        print(f'{hero}')
        print(f'HP: {current_hp}')
        print(f'MP: {current_mp}')


loop_range = int(input())
MAX_HP = 100
MAX_MP = 200
heroes_lst = {}
heroes_lst = add_heroes(loop_range, heroes_lst, MAX_HP, MAX_MP)
process_commands(MAX_HP, MAX_MP, heroes_lst)

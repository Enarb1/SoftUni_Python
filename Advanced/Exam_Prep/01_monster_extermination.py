from collections import deque

def result_print(soldiers, monsters, killed_monsters):

    if not monsters:
        print("All monsters have been killed!")
    if not soldiers:
        print("The soldier has been defeated.")

    print(f"Total monsters killed: {killed_monsters}")


def monster_fights_back(soldier, monster, soldiers, monsters):
    monster -= soldier
    monsters.append(monster)

    return soldiers, monsters

def kill_monster(soldier, monster, soldiers, monsters):
    if soldiers:
        soldiers[-1] += soldier - monster
    else:
        if soldier - monster > 0:
            soldiers.append(soldier - monster)

    return soldiers, monsters


def get_monsters():
    return deque([int(m) for m in input().split(",")])

def get_soldiers():
    return [int(s) for s in input().split(",")]

def monster_extermination(monsters, soldiers):
    killed_monsters = 0

    while monsters and soldiers:
        monster = monsters.popleft()
        soldier = soldiers.pop()

        if soldier >= monster:
            killed_monsters += 1
            kill_monster(soldier, monster, soldiers, monsters)
        else:
            monster_fights_back(soldier, monster, soldiers, monsters)

    return result_print(soldiers, monsters,killed_monsters)


monsters_armour = get_monsters()
soldier_strike = get_soldiers()
monster_extermination(monsters_armour, soldier_strike)

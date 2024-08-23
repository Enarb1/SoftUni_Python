def add_dragon(dragons, dragon_type, name, damage, health, armour):
    if dragon_type not in dragons.keys():
        dragons[dragon_type] = {}
    dragons[dragon_type][name] = {'damage': damage, 'health': health, 'armour': armour}


def print_dragons():
    for dragon_type, dragon_info in dragons.items():
        average_damage = sum(d['damage'] for d in dragon_info.values()) / len(dragon_info)
        average_health = sum(d['health'] for d in dragon_info.values()) / len(dragon_info)
        average_armour = sum(d['armour'] for d in dragon_info.values()) / len(dragon_info)

        print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armour:.2f})")

        for name in sorted(dragon_info):
            damage = dragon_info[name]["damage"]
            health = dragon_info[name]["health"]
            armour = dragon_info[name]["armour"]
            print(f"-{name} -> damage: {damage}, health: {health}, armor: {armour}")


dragons = {}
loop_range = int(input())

for _ in range(loop_range):
    dragon_type,dragon_name,damage, health, armour = input().split()
    if damage == 'null':
        damage = 45
    damage = int(damage)
    if health == 'null':
        health = 250
    health = int(health)
    if armour == 'null':
        armour = 10
    armour = int(armour)
    add_dragon(dragons,dragon_type,dragon_name,damage,health,armour)
print_dragons()




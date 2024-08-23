command_lst = input().split("|")
health = 100
bitcoins = 0
room = 0
for command in command_lst:
    command_parts = command.split()
    room += 1
    if command_parts[0] == 'potion':
        previous_health = health
        heal_amount = int(command_parts[1])
        health += heal_amount
        if health > 100:
            health = 100
            heal_amount = abs(previous_health - 100)
        print(f"You healed for {heal_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command_parts[0] == 'chest':
        bitcoin_amount = int(command_parts[1])
        bitcoins += bitcoin_amount
        print(f"You found {bitcoin_amount} bitcoins.")
    else:
        monster_type = command_parts[0]
        hit_power = int(command_parts[1])
        health -= hit_power
        if health <= 0:
            print(f"You died! Killed by {monster_type}.")
            print(f"Best room: {room}")
            break
        else:
            print(f"You slayed {monster_type}.")

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")




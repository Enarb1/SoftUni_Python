def add_plants(plants, loop_range):

    for _ in range(loop_range):
        plant, rarity = input().split("<->")
        if plant not in plants.keys():
            plants[plant] = {}
        plants[plant] = {'rarity': rarity, 'rating': []}
    return plants


def rate(plants, plant, rating):

    if plant in plants.keys():
        plants[plant]['rating'].append(int(rating))
        return plants
    print('error')


def update(plants, plant, rarity):
    if plant in plants.keys():
        plants[plant]['rarity'] = rarity
        return plants
    print('error')


def reset(plants, plant):
    if plant in plants.keys():
        plants[plant]['rating'] = []
        return plants
    print('error')


plants = {}
loop_range = int(input())
add_plants(plants, loop_range)

while True:
    command = input()
    if command == 'Exhibition':
        break

    line = command.split(': ')

    if line[0] == 'Rate':
        plant_type, num = line[1].split(" - ")
        rate(plants, plant_type, num)
    elif line[0] == 'Update':
        plant_type, num = line[1].split(" - ")
        update(plants, plant_type, num)
    elif line[0] == 'Reset':
        plant_type = line[1]
        reset(plants, plant_type)

print("Plants for the exhibition:")
for plant in plants.keys():
    rarity = plants[plant]['rarity']
    if len(plants[plant]['rating']) > 0:
        average = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    else:
        average = 0
    print(f'- {plant}; Rarity: {rarity}; Rating: {average:.2f}')
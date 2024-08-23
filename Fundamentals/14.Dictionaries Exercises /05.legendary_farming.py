materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

item_obtained = False

while not item_obtained:
    command = input().lower().split()
    for index in range(0, len(command), 2):
        quantity = int(command[index])
        material = command[index + 1]

        if material in materials.keys():
            materials[material] += quantity
            if materials[material] >= 250:
                materials[material] -= 250
                print(f"{legendary_items[material]} obtained!")
                item_obtained = True
                break
        else:
            if material not in junk_materials.keys():
                junk_materials[material] = 0
            junk_materials[material] += quantity

for material, quantity in materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")


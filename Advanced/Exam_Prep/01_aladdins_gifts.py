from collections import deque

materials = [int(m) for m in input().split()]
magic_levels = deque([int(x) for x in input().split()])

item_mapper ={
    range(100, 199): "Gemstone",
    range(200, 299): "Porcelain Sculpture",
    range(300, 399): "Gold",
    range(400, 499): "Diamond Jewellery",
}
crafted = {}


while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    if (material + magic) < 100:
        if (material + magic) % 2 == 0:
            magic *= 3
        else:
            magic *= 2
        material *= 2

    elif (material + magic) > 499:
        magic /= 2
        material /= 2

    value = int(material) + int(magic)
    gift_crafted = next((item for key, item in item_mapper.items() if value in key), None)

    if gift_crafted:
        crafted[gift_crafted] = crafted.get(gift_crafted, 0) + 1

if (("Gemstone" in crafted.keys() and "Porcelain Sculpture" in crafted.keys())
        or ("Gold" in crafted.keys() and "Diamond Jewellery" in crafted.keys())):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

if crafted:
    print('\n'.join(f"{present}: {amount}" for present, amount in crafted.items()))






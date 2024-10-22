from collections import deque

COOKIE = 1

elf_energy = deque([int(e) for e in input().split()])
materials = deque([int(m) for m in input().split()])

toys_count = 0
energy_used = 0
turns = 0
while elf_energy and materials:
    turns += 1
    energy = elf_energy.popleft()

    if energy < 5:
        continue

    material = materials.pop()
    needed_material = material
    toys_made = 0

    if turns % 3 == 0:
       needed_material = material * 2

    if energy >= needed_material:
        energy -= needed_material
        energy_used += needed_material
        energy += COOKIE if turns % 5 != 0 else 0
        toys_made += 2 if turns % 3 == 0 else 1
    else:
        energy += energy
        materials.appendleft(material)

    elf_energy.append(energy)

    if turns % 5 == 0:
        continue

    toys_count += toys_made

print(f"Toys: {toys_count}")
print(f"Energy: {energy_used}")
if elf_energy:
    print(f"Elves left: {', '.join(map(str, elf_energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
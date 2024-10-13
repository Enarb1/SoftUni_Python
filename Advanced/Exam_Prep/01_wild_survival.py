from collections import deque

bee_hive = deque(list(map(int, input().split())))
bee_eaters_nest = list(map(int, input().split()))


while bee_hive and bee_eaters_nest:

    bees = bee_hive.popleft()
    bee_eaters = bee_eaters_nest.pop()
    loop_range = bee_eaters

    for _ in range(loop_range):
        if bees >= 7:
            bee_eaters -= 1
        bees -= 7
        if bees <= 0:
            break
    if bee_eaters > 0:
        bee_eaters_nest.append(bee_eaters)
    if bees > 0:
        bee_hive.append(bees)


print("The final battle is over!")
if not bee_hive and not bee_eaters_nest:
    print("But no one made it out alive!")

if bee_hive:
    print(f"Bee groups left: {', '.join(str(x) for x in bee_hive)}")
if bee_eaters_nest:
    print(f"Bee-eater groups left: {', '.join(str(x) for x in bee_eaters_nest)}")

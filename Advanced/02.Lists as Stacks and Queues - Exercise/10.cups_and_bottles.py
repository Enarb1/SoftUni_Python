from collections import deque

cups = deque(map(int, input().split()))
bottles = [int(b) for b in input().split()]

wasted_water = 0

while bottles and cups:
    bottle = bottles.pop()
    cup = cups.popleft()
    if cup <= bottle:
        wasted_water += bottle - cup
    else:
        cups.appendleft(cup - bottle)

if len(cups) == 0:
    print("Bottles:", *bottles)
else:
    print("Cups:", * cups)
print(f'Wasted litters of water: {wasted_water}')


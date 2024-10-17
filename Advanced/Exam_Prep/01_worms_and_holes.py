from collections import deque

DECREASE = 3

worms = [int(n) for n in input().split()]
holes = deque(map(int, input().split()))

matches = 0
total_worms = len(worms.copy())

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1

    else:
        worm -= DECREASE
        if worm > 0:
            worms.append(worm)

print(f"Matches: {matches}") if matches else print("There are no matches.")

if not worms:
    if total_worms == matches:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

else:
    print(f"Worms left: {', '.join(str(w) for w in worms)}")


if holes:
    print(f"Holes left: {', '.join(str(h) for h in holes)}")
else:
    print("Holes left: none")
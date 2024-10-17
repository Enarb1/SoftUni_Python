from collections import deque

fuel = [int(f) for f in input().split()]
additional_fuel = deque([int(a) for a in input().split()])
amount_needed = deque(int(l) for l in input().split())

current_latitude = 0
reached = []


while amount_needed:
    current_latitude += 1
    current_fuel = fuel.pop()
    current_add_fuel = additional_fuel.popleft()
    needed = amount_needed.popleft()

    result = current_fuel - current_add_fuel

    if result >= needed:
        reached.append(f"Altitude {current_latitude}")
        print(f"John has reached: {reached[-1] }")
    else:
        amount_needed.appendleft(needed)
        print(f"John did not reach: Altitude {current_latitude}")
        break

if amount_needed:
    print("John failed to reach the top.")
    if len(reached) == 0:
        print("John didn't reach any altitude.")
    else:
        print(f"Reached altitudes: {', '.join(reached)}")
else:
    print("John has reached all the altitudes and managed to reach the top!")

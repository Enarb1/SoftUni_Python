STEPS_GOAL = 10_000

total_steps = 0

while total_steps < STEPS_GOAL:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    steps = int(command)
    total_steps += steps

diff = abs(total_steps - STEPS_GOAL)

if total_steps >= STEPS_GOAL:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")




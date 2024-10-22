from collections import deque

GOAL_VALUE = 100
DECREASE_VALUE = 10

strength_nums = [int(s) for s in input().split()]
accuracy_nums = deque([int(a) for a in input().split()])

goals_scored = 0


while strength_nums and accuracy_nums:
    strength = strength_nums.pop()
    accuracy = accuracy_nums.popleft()

    total = strength + accuracy

    if total == GOAL_VALUE:
        goals_scored += 1

    elif total < GOAL_VALUE:
        if strength < accuracy:
            accuracy_nums.appendleft(accuracy)
        elif strength > accuracy:
            strength_nums.append(strength)
        else:
            strength_nums.append(total)

    else:
        strength -= DECREASE_VALUE
        strength_nums.append(strength)
        accuracy_nums.append(accuracy)


if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
else:
    if goals_scored > 3:
        print("Paul performed remarkably well!")
    else:
        print("Paul failed to make a hat-trick.")

if goals_scored:
    print(f"Goals scored: {goals_scored}")
if strength_nums:
    print(f"Strength values left: {', '.join(map(str, strength_nums))}")
if accuracy_nums:
    print(f"Accuracy values left: {', '.join(map(str, accuracy_nums))}")


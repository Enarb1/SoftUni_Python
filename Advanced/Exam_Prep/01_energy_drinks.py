from collections import deque

MAX_CAFFEINE = 300
REMOVE_CAFFEINE = 30

def final_print(energy_drinks,current_caffeine):

    if energy_drinks:
        message = f"Drinks left: {', '.join(map(str, energy_drinks))}"
    else:
        message = "At least Stamat wasn't exceeding the maximum caffeine."
    message += f"\nStamat is going to sleep with {current_caffeine} mg caffeine."

    return message

def energy(caffeine_mgs, energy_drinks):

    current_caffeine = 0

    while caffeine_mgs and energy_drinks:
        caffeine = caffeine_mgs.pop()
        energy_drink = energy_drinks.popleft()

        total_caffeine = caffeine * energy_drink

        if not (current_caffeine + total_caffeine) > MAX_CAFFEINE:
            current_caffeine += total_caffeine
        else:
            current_caffeine -= REMOVE_CAFFEINE
            energy_drinks.append(energy_drink)
            if current_caffeine < 0:
                current_caffeine = 0

    return final_print(energy_drinks, current_caffeine)

caffeine_milligrams = [int(c) for c in input().split(", ")]
energy_drinks_total = deque([int(e) for e in input().split(", ")])
print(energy(caffeine_milligrams, energy_drinks_total))

def game(energy):
    battles_won = 0
    while True:
        command = input()
        if command == "End of battle":
            return f"Won battles: {battles_won}. Energy left: {energy}"

        distance = int(command)

        if energy >= distance:
            battles_won += 1
            energy -= distance
            if battles_won % 3 == 0:
                energy += battles_won
        else:
            return f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy"


initial_energy = int(input())
result = game(initial_energy)
print(result)
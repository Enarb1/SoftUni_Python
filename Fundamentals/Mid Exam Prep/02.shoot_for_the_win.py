def shots_on_target(targets, shots_lst):
    targets_hit = []

    for target in shots_lst:
        if target <= len(targets) - 1:
            if target not in targets_hit:
                value = targets[target]
                targets_hit.append(target)
                targets.pop(target)
                targets.insert(target, -1)
                for index, num in enumerate(targets):
                    if num != -1:
                        if num > value:
                            new_num = num - value
                            targets.pop(index)
                            targets.insert(index,new_num)
                        elif num <= value:
                            new_num = num + value
                            targets.pop(index)
                            targets.insert(index, new_num)

    result = " ".join(map(str,targets))

    return f"Shot targets: {len(targets_hit)} -> {result}"


sequence = list(map(int,input().split()))
shots = []
target_shots = 0
while True:
    command = input()
    if command == 'End':
        break
    target_shots += 1
    shots.append(int(command))

print(shots_on_target(sequence,shots))



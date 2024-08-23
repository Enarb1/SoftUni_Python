start = int(input())
finish = int(input())
magic_number = int(input())

combinations = 0
combination_found = False

for n1 in range(start, finish + 1):
    for n2 in range(start, finish + 1):
        combinations += 1
        if n1 + n2 == magic_number:
            print(f"Combination N:{combinations} ({n1} + {n2} = {magic_number}) ")
            combination_found = True
            exit()
if not combination_found:
    print(f"{combinations} combinations - neither equals {magic_number}")

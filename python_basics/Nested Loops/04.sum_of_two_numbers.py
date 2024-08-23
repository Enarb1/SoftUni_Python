start = int(input())
finish = int(input())
magic_number = int(input())

combinations = 0
breakpoint = False

for a in range(start,finish +1 ):
    for b in range(start,finish + 1):
        combinations += 1
        if a + b == magic_number:
            print(f"Combination N:{combinations} ({a} + {b} = {magic_number})")
            breakpoint = True
    if breakpoint:
        break
else:
    print(f"{combinations} combinations - neither equals {magic_number}")


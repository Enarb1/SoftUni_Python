detergent_bottles = int(input())
detergent_mls_total = detergent_bottles * 750

plates_total = 0
pots_total = 0
cycles = 0

while detergent_mls_total >= 0:
    command = input()
    if command == "End":
        print("Detergent was enough!")
        print(f"{plates_total} dishes and {pots_total} pots were washed.")
        print(f"Leftover detergent {detergent_mls_total} ml.")
        break
    else:
        cycles += 1
        if cycles == 3:
            pots = int(command)
            pots_total += pots
            detergent_mls_total -= pots * 15
            cycles = 0
        else:
            plates = int(command)
            plates_total += plates
            detergent_mls_total -= plates * 5
else:
    print(f"Not enough detergent, {abs(detergent_mls_total)} ml. more necessary!")







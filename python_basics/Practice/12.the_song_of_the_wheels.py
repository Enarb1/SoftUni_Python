magic_number = int(input())

numbers = 0
password = ""
combination_found = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b) + (c * d) == magic_number:
                        print(f"{a}{b}{c}{d}", end=" ")
                        numbers += 1
                        if numbers == 4:
                            combination_found = True
                            password = f"{a}{b}{c}{d}"
if combination_found:
    print(f"\nPassword: {password}")
if not combination_found:
    print("\nNo!")

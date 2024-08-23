magic_number = int(input())
counter = 0
for a in range(0,magic_number + 1):
    for b in range(0, magic_number + 1):
        for c in range (0, magic_number + 1):
            if a + b + c == magic_number:
                counter += 1

print(counter)
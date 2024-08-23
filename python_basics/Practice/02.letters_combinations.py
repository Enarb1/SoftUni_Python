start_letter = input()
end_letter = input()
skip_letter = input()

combinations = 0

for l1 in range(ord(start_letter), ord(end_letter) + 1):
    for l2 in range(ord(start_letter), ord(end_letter)+ 1):
        for l3 in range(ord(start_letter), ord(end_letter) + 1):
            if chr(l1) != skip_letter and chr(l2) != skip_letter and chr(l3) != skip_letter:
                print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end=" ",)
                combinations += 1
print(combinations)
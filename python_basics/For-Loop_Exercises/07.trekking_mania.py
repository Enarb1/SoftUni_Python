musala = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(int(input())):
    group = int(input())

    if group < 6:
        musala += group
    elif group < 13:
        monblanc += group
    elif group < 26:
        kilimandjaro += group
    elif group < 41:
        k2 += group
    else:
        everest += group

total_people = musala + monblanc + kilimandjaro + k2 + everest

print(f"{musala / total_people * 100:.2f}%")
print(f"{monblanc / total_people * 100:.2f}%")
print(f"{kilimandjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")




capacity = int(input())
fans = int(input())

a = 0
b = 0
v = 0
g = 0

for _ in range(1, fans + 1):
    sector = input()
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1
print(f"{(a / fans) * 100:.2f}%")
print(f"{(b / fans) * 100:.2f}%")
print(f"{(v / fans) * 100:.2f}%")
print(f"{(g / fans) * 100:.2f}%")
print(f"{(fans / capacity) * 100:.2f}%")
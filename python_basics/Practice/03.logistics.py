loads = int(input())
total_weight = 0
bus = 0
truck = 0
train = 0
total_price = 0

for _ in range(1,loads + 1):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        bus += weight
        price = weight * 200
    if 3 < weight < 12:
        truck += weight
        price = weight * 175
    if weight >= 12:
        train += weight
        price = weight * 120

    total_price += price

print(f"{total_price / total_weight:.2f}")
print(f"{bus / total_weight * 100:.2f}%")
print(f"{truck / total_weight * 100:.2f}%")
print(f"{train / total_weight * 100:.2f}%")
from collections import deque

packages = [int(p) for p in input().split()]
couriers = deque([int(c) for c in input().split()])

total_delivered_weight = 0

while packages and couriers:
    pack = packages.pop()
    courier = couriers.popleft()

    if courier >= pack:
        courier -= pack * 2
        if courier > 0:
            couriers.append(courier)
        total_delivered_weight += pack
    else:
        pack -= courier
        packages.append(pack)
        total_delivered_weight += courier

print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver "
          f"the following packages: {', '.join(str(p) for p in packages)}")
else:
    print(f"Couriers are still on duty: {', '.join(str(c) for c in couriers)} "
          f"but there are no more packages to deliver.")


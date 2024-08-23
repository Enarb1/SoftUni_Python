from collections import deque

packages = [int(x) for x in input().split()]
courier_capacity = deque(int(x) for x in input().split())

total_weight = 0

while packages and courier_capacity:
    package = packages.pop()
    courier = courier_capacity.popleft()

    if courier >= package:
        if courier > package:
            new_courier = courier - (package * 2)
            if new_courier > 0:
                courier_capacity.append(new_courier)
        total_weight += package
    else:
        packages.append(package - courier)
        total_weight += courier

print(f"Total weight: {total_weight} kg")
if not packages and not courier_capacity:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and len(courier_capacity) == 0:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages:"
          f" {', '.join(str(x) for x in packages)}")
elif courier_capacity and len(packages) == 0:
    print(f"Couriers are still on duty:  {', '.join(str(x) for x in courier_capacity)}but there are no more packages "
          f"to deliver.")

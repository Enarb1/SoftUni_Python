from collections import deque

water = int(input())
water_que = deque()

name = input()

while name != 'Start':
    water_que.append(name)
    name = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        liters_requested = int(data[0])
        person = water_que.popleft()
        if water >= liters_requested:
            water -= liters_requested
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
    elif len(data) > 1:
        _, liters = data
        water += int(liters)
    command = input()
print(f'{water} liters left')

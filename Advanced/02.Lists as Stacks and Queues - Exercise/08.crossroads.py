from collections import deque

green_light_time = int(input())
free_window = int(input())

cars_que = deque()
crash = False
cars_passed_count = 0
while True:
    data = input()
    if crash:
        break
    if data == 'END':
        break
    elif data == 'green':
        time_left_to_enter = green_light_time
        while time_left_to_enter > 0:
            if cars_que:
                car = cars_que.popleft()
                if len(car) > time_left_to_enter:
                    if len(car[time_left_to_enter:]) > free_window:
                        crash = True
                        hit = car[time_left_to_enter + free_window]
                        print('A crash happened!')
                        print(f'{car} was hit at {hit}.')
                        break
                    else:
                        cars_passed_count += 1
                else:
                    cars_passed_count += 1
                time_left_to_enter -= len(car)
            else:
                break
    else:
        cars_que.append(data)

if not crash:
    print('Everyone is safe.')
    print(f'{cars_passed_count} total cars passed the crossroads.')





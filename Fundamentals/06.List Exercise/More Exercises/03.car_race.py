input_list = input().split(" ")
times_list = []
left_car_total_time = 0
right_car_total_time = 0

for time in input_list:
    times_list.append(int(time))

finsh_line = len(times_list) // 2

for time_left_car in times_list[:finsh_line]:
    if time_left_car == 0:
        left_car_total_time = left_car_total_time * 0.8
    else:
        left_car_total_time += time_left_car

for time_right_car in reversed(times_list[finsh_line + 1:]):
    if time_right_car == 0:
        right_car_total_time = right_car_total_time * 0.8
    else:
        right_car_total_time += time_right_car
left_car = "left"
right_car = "right"
if left_car_total_time < right_car_total_time:
    winner = left_car
    winner_time = left_car_total_time
else:
    winner = right_car
    winner_time = right_car_total_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")



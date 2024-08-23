exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_total_minutes = (exam_hour * 60) + exam_min
arrival_total_minutes = (arrival_hour * 60) + arrival_min
hours = 0
minutes = 0
time_of_arrival = arrival_total_minutes - exam_total_minutes

if time_of_arrival == 0:
    print("On time")
    exit()
elif time_of_arrival < 0 and time_of_arrival >= -30:
    print("On time")
    print(f"{abs(time_of_arrival)} minutes before the start")
    exit()
elif time_of_arrival < -59:
    hours = abs(time_of_arrival) // 60
    minutes = abs(time_of_arrival) % 60
    if minutes < 10:
        print("Early")
        print(f"{hours}:0{minutes} hours before the start")
        exit()
    else:
        print("Early")
        print(f"{hours}:{minutes} hours before the start")
        exit()
elif time_of_arrival < -30:
    print("Early")
    print(f"{abs(time_of_arrival)} minutes before the start")
    exit()
elif time_of_arrival > 59:
    hours = time_of_arrival // 60
    minutes = time_of_arrival % 60
    if minutes < 10:
        print("Late")
        print(f"{hours}:0{minutes} hours after the start")
        exit()
    else:
        print("Late")
        print(f"{hours}:{minutes} hours after the start")
else:
    print("Late")
    print(f"{time_of_arrival} minutes after the start")


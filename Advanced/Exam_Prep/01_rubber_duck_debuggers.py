from collections import deque

time_needed_for_tasks = deque([int(n) for n in input().split()])
tasks = [int(t) for t in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky" :  0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
         }

mapper = {
    (0, 60): "Darth Vader Ducky",
    (61, 120): "Thor Ducky",
    (121, 180): "Big Blue Rubber Ducky",
    (181, 240): "Small Yellow Rubber Ducky"
}


while time_needed_for_tasks and tasks:
    time = time_needed_for_tasks.popleft()
    task = tasks.pop()
    value = time * task

    for (start, end), duck in mapper.items():
        if start <= value <= end:
            ducks[duck] += 1
            break
    else:
        task = task - 2
        tasks.append(task)
        time_needed_for_tasks.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks.items():
    print(f"{duck}: {count}")
def add_stop(tour, index, input_string):
    return tour[:index] + input_string + tour[index:]


def remove_stop(tour, start, end):
    return tour[:start] + tour[end + 1:]


def switch(tour, old, new):
    return tour.replace(old, new)


tour = input()

while True:
    command = input()
    if command == 'Travel':
        break

    line = command.split(":")
    action = line[0]
    if action == 'Add Stop':
        index = int(line[1])
        string_input = line[2]
        if index <= len(tour):
            tour = add_stop(tour, index, string_input)
    elif action == 'Remove Stop':
        start = int(line[1])
        end = int(line[2])
        if start < len(tour) and end < len(tour):
            tour = remove_stop(tour, start, end)
    elif action == 'Switch':
        old = line[1]
        new = line[2]
        if old in tour:
            tour = switch(tour, old, new)
    print(tour)
print(f'Ready for world tour! Planned stops: {tour}')

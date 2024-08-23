
def wagon(num_of_wagons):

    train = [0 for _ in range(num_of_wagons)]

    while True:
        command_list = input().split()
        command = command_list[0]

        if command == 'End':
            break
        elif command == 'add':
            passengers = int(command_list[1])
            train[-1] += passengers
        elif command == 'insert':
            index = int(command_list[1])
            passengers = int(command_list[2])
            train[index] += passengers
        elif command == 'leave':
            index = int(command_list[1])
            passengers = int(command_list[2])
            train[index] -= passengers

    return train


wagons = int(input())
final_train = wagon(wagons)
print(final_train)
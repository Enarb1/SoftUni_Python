def not_enough_chairs(num_of_chairs, num_of_people, room_num):
    needed_chairs = abs(num_of_chairs - num_of_people)

    return f'{needed_chairs} more chairs needed in room {room_num}'


rooms_to_check = int(input())
room = 0
free_chairs = 0
enough_space = True
while rooms_to_check != 0:
    room += 1
    command = input().split()
    chairs = command[0]
    people = int(command[1])
    if len(chairs) >= people:
        free_chairs += len(chairs) - people
    else:
        enough_space = False
        print(not_enough_chairs(len(chairs), people, room))

    rooms_to_check -= 1


if enough_space == True:
    print(f"Game On, {free_chairs} free chairs left")

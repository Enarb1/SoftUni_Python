width_room = int(input())
lenght_room = int(input())
height_room = int(input())

room_size = width_room * lenght_room * height_room

taken_size = 0

while True:
    command = input()
    if command == "Done":
        print(f"{room_size - taken_size} Cubic meters left.")
        break
    else:
        command = int(command)
        taken_size += command
        if taken_size >= room_size:
            print(f"No more free space! You need {taken_size - room_size} Cubic meters more.")
            break
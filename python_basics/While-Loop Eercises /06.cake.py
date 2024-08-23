cake_width = int(input())
cake_lenght = int(input())

cake_size = cake_lenght * cake_width
pieces_taken = 0

while True:
    command = input()
    if command == "STOP":
        print(f"{cake_size-pieces_taken} pieces are left.")
        break
    else:
        command = int(command)
        pieces_taken += command
        if pieces_taken >= cake_size:
            print(f"No more cake left! You need {abs(cake_size - pieces_taken)} pieces more.")
            break


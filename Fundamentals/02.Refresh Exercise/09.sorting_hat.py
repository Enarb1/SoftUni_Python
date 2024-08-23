command = input()

while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        exit()
    else:
        name = command
        if len(name) < 5:
            print(f"{name} goes to Gryffindor.")
        elif len(name) == 5:
            print(f"{name} goes to Slytherin.")
        elif len(name) == 6:
            print(f"{name} goes to Ravenclaw.")
        else:
            print(f"{name} goes to Hufflepuff.")
    name = command
    command = input()
print("Welcome to Hogwarts.")
while True:
    command = input()
    if command == "End":
        break

    destination = command
    budget_needed = float(input())
    saved_money = 0
    while True:
        saved_money += float(input())
        if saved_money >= budget_needed:
            print(f"Going to {destination}!")
            break





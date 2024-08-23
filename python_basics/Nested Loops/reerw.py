
while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())

while True:
    saved_money = 0
    for destination, budget in destinations:
        if budget <= saved_money:
            print(f"Going to {destination}!")
            del destinations[destination]
            break
    else:
        saved = float(input())
        if saved < 0:
            print()
            continue
        saved_money += saved
        continue



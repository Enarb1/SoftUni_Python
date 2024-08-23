budget = int(input())

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        price = int(command)
        budget -= price
        if budget < 0:
            print("You went in overdraft!")
            break

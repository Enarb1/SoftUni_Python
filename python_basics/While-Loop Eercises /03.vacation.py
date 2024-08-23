money_needed = float(input())
balance = float(input())
days = 0
spend_days = 0

while True:
    command = input()
    money = float(input())
    if command == "spend":
        balance -= money
        spend_days += 1
        days += 1
        if balance < 0:
            balance = 0

        if spend_days == 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break


    if command == "save":
        balance += money
        spend_days = 0
        days += 1
        if balance >= money_needed:
            print(f"You saved the money for {days} days.")
            break





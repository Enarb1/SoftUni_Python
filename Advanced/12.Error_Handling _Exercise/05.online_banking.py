class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


def check_send_money():
    if money_balance < money:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

    if pin_code != pin:
        raise PINCodeError("Invalid PIN code")

    if age < LEGAL_AGE:
        raise UnderageTransactionError(f"You must be {LEGAL_AGE} years or older to perform online transactions")

    return True


def check_receive_money():
    if money < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")

    return True


def receive_money(balance, amount):
    while True:
        try:
            balance += (amount / 2)
        except ZeroDivisionError:
            return "Amount should  be bigger than 0!"

        print(f"{(amount / 2):.2f} money went straight into the bank account")

        return balance


LEGAL_AGE = 18

input_line = input().split(", ")
pin_code = input_line[0]
money_balance = float(input_line[1])
age = int(input_line[2])

while True:
    command = input()
    if command == "End":
        break

    line_data = command.split("#")
    action = line_data[0]

    if action == "Send Money":
        money = float(line_data[1])
        pin = line_data[2]

        if check_send_money():
            money_balance -= money
            print(f"Successfully sent {money:.2f} money to a friend")
            print(f"There is {money_balance:.2f} money left in the bank account")

    elif action == "Receive Money":
        money = float(line_data[1])

        if check_receive_money():
            money_balance = receive_money(money_balance, money)





ACCOUNT_BALANCE = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    current_sum = float(text)

    if current_sum >= 0:
        ACCOUNT_BALANCE += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {ACCOUNT_BALANCE:.2f}")


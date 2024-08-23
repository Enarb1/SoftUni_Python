expected_sum = int(input())

sum_gathered = 0
sale = 0
cash_payment = 0
cash_gathered = 0
cc_payment = 0
cc_gathered = 0
successful_payments = 0

while True:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        price = int(command)
        if sale == 0:
            sale += 1
            if price <= 100:
                print("Product sold!")
                sum_gathered += price
                cash_gathered += price
                cash_payment += 1
                successful_payments += 1
            else:
                print("Error in transaction!")
        elif sale == 1:
            sale = 0
            if price < 10:
                print("Error in transaction!")
            else:
                print("Product sold!")
                sum_gathered += price
                cc_gathered += price
                cc_payment += 1
                successful_payments += 1
        if sum_gathered >= expected_sum:
            print(f"Average CS: {cash_gathered / cash_payment:.2f}")
            print(f"Average CC: {cc_gathered / cc_payment:.2f}")
            break
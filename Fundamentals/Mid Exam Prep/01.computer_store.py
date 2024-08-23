total_price = 0
discount = 0
while True:
    tax = total_price * 0.2
    command = input()
    if command == "special":
        discount = (total_price + tax) * 0.1
        final = (total_price + tax) - discount
        break
    elif command == 'regular':
        final = total_price + tax
        break
    else:
        command = float(command)
    if command < 0:
        print("Invalid price!")
    else:
        total_price += command

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {final:.2f}$")

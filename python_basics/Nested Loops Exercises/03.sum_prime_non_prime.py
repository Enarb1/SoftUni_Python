sum_prime = 0
sum_other = 0

while True:
    command = input()
    if command != "stop":
        number = int(command)
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                sum_prime += number
            else:
                sum_other += number
        elif number < 0:
            print("Number is negative.")
    else:
        break

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_other}")


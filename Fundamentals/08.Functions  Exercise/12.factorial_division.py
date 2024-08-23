def calculate_factorial(some_number: int) -> int:
    for current_number in range(1, some_number):
        some_number *= current_number
    return some_number


first_number = int(input())
second_number = int(input())
first_factorial = calculate_factorial(first_number)
second_factorial = calculate_factorial(second_number)
print(f"{first_factorial / second_factorial:.2f}")
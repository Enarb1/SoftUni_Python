n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0
    sum_of_digits += number
    if number > 9:
        sum_of_digits = 0
        number_string = str(number)
        for digit in number_string:
            sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")

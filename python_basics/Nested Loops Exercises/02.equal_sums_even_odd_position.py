first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1 ):
    number_string = str(i)
    even_sum = 0
    odd_sum = 0
    is_even = 1

    for digit in number_string:
        if is_even % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

        is_even += 1

    if even_sum == odd_sum:
        print(i, end=" ")



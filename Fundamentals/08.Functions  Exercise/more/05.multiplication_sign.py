def result_type(number1, number2, number3):
    numbers = [number1, number2, number3]
    if 0 in numbers:
        return 'zero'

    negative = 0

    for num in numbers:
        if num < 0:
            negative += 1
    if negative % 2 == 1:
        return 'negative'
    else:
        return 'positive'


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(result_type(num1, num2, num3))

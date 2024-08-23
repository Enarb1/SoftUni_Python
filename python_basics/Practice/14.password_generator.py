n = int(input())
l = int(input())

for digit1 in range(1, n):
    for digit2 in range(1, n):
        for letter1 in range(97, 97 + l):
            for letter2 in range(97, 97 + l):
                for digit3 in range(digit1 + 1, n + 1):
                    if digit3 > digit2:
                        print(f"{digit1}{digit2}{chr(letter1)}{chr(letter2)}{digit3}", end=" ")
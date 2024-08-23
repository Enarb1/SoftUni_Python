key = int(input())
lines = int(input())

for line in range(1, lines + 1):
    current_letter = input()
    letter = ord(current_letter) + key
    print(chr(letter), end="")

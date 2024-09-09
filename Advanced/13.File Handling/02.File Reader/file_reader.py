import re

try:
    with open("numbers.txt") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found")

total = 0

for line in lines:
    num = ''.join(re.findall(r'\b\d+\b', line))
    total += int(num)

print(total)




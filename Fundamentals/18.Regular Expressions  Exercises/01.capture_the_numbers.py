import re

while True:
    line = input()
    if line == '':
        break

    pattern = r'\d+'
    matches = re.findall(pattern, line)
    for num in matches:
        print(num,end=' ')


import re

n = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]'

for _ in range(n):
    line = input()
    if re.match(pattern, line):
        matches = re.finditer(pattern, line)
        for match in matches:
            command = match.group(1)
            message = " ".join(str(ord(char)) for char in match.group(2))
            print(f'{command}: {message}')
    else:
        print('The message is invalid')

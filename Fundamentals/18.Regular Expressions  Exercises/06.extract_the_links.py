import re

while True:
    line = input()
    if line == '':
        break

    pattern = r'\b([w]{3}).([a-zA-Z0-9-]+)([.][a-z]+)([.a-z]+)?'
    matches = re.finditer(pattern, line)

    for link in matches:
        print(link.group(0))

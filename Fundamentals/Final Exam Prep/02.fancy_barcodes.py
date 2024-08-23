import re

loop_range = int(input())

for _ in range(loop_range):
    text = input()
    pattern = re.compile(r'@[#]+([A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+')
    match = pattern.search(text)

    if match:
        group = ''
        for char in match.group(1):
            if char.isdigit():
                group += char
        if group == '':
            group = '00'

        print(f'Product group: {group}')
    else:
        print("Invalid barcode")
import re

pattern = re.compile(r'%([A-Z][a-z]+)%.*?<(\w+)>.*?\|(\d+)\|.*?(\d+(?:\.\d+)?)\$')
total = 0
while True:
    order = []
    command = input()
    if command == 'end of shift':
        break
    text = command
    match = pattern.search(text)

    if match:
        name = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))

        total_price = price * count
        total += price * count

        print(f'{name}: {product} - {total_price:.2f}')
print(f'Total income: {total:.2f}')

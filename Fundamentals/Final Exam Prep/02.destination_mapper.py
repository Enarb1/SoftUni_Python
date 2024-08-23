import re
text = input()

destinations = []
points = 0

pattern = r'[=]([A-Z][a-zA-Z]{2,})[=]|[\/]([A-Z][a-zA-Z]{2,})[\/]'
matches = re.finditer(pattern, text)

for match in matches:
    if match.group(1):
        destinations.append(match.group(1))
        points += len(match.group(1))
    elif match.group(2):
        destinations.append(match.group(2))
        points += len(match.group(2))

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')
import re

loop_range = int(input())
attacked =[]
destroyed = []
for _ in range(loop_range):
    message = input()
    count_pattern = r'[starSTAR]'
    count = int(len(re.findall(count_pattern, message)))
    new_message = ''
    for char in message:
        new_char = chr(ord(char) - count)
        new_message += new_char
    pattern = re.compile(r'@([A-Za-z]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!([A|D])![^@\-!:>]*->([0-9]+)')
    match = pattern.search(new_message)
    if match:
        planet = match.group(1)
        population = match.group(2)
        attack_type = match.group(3)
        soldier_count = match.group(4)
        if attack_type == 'A':
            attacked.append(planet)
        elif attack_type == 'D':
            destroyed.append(planet)

print(f'Attacked planets: {len(attacked)}')
if len(attacked) > 0:
    for name in sorted(attacked):
        print(f'-> {name}')
print(f'Destroyed planets: {len(destroyed)}')
if len(destroyed) > 0:
    for name in sorted(destroyed):
        print(f'-> {name}')

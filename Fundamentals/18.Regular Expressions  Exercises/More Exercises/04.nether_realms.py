import re

demons = sorted(re.split(r'\s*,\s*', input()))
health_pattern = r'[^0-9\+*\/.-]'
damage_pattern = r'([+|-]?\d*\.?\d+)'
for demon in demons:
    health_match = re.findall(health_pattern, demon)
    damage_match = re.findall(damage_pattern, demon)
    total_health = sum(ord(element) for element in health_match)
    total_damage = sum(float(num) for num in damage_match)
    if total_damage > 0:
        for sign in demon:
            if sign == "*":
                total_damage *= 2
            elif sign == '/':
                total_damage /= 2

    print(f'{demon} - {total_health} health, {total_damage:.2f} damage')
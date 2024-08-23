import re


def purchase(command, bought, money):
    pattern = r'>>([a-zA-Z_]+)<<([0-9\.]+)!([0-9]+)'

    if re.match(pattern, command):
        matches = re.finditer(pattern, command)
        for match in matches:
            furniture = match.group(1)
            cost = float(match.group(2))
            qty = int(match.group(3))
            bought.append(furniture)
            money.append(cost * qty)


furniture_bought = []
money_spent = []
while True:
    command = input()
    if command == 'Purchase':
        break
    purchase(command, furniture_bought, money_spent)

total = sum(money_spent)
print('Bought furniture:')
for item in furniture_bought:
    print(item)
print(f'Total money spend: {total:.2f}')

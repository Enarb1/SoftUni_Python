input_data = input().split()
bakery = {}

for key_value in range(0, len(input_data), 2):
    key = input_data[key_value]
    value = input_data[key_value + 1]
    bakery[key] = int(value)

print(bakery)


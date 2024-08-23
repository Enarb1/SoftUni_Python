resources = {}

while True:
    command = input()
    if command == 'stop':
        break
    resource_type = command
    quantity = int(input())
    if resource_type not in resources:
        resources[resource_type] = 0
    resources[resource_type] += quantity

for res_type, value in resources.items():
    print(f"{res_type} -> {value}")

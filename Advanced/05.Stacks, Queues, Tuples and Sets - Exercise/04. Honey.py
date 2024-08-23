from collections import deque

bees = deque(map(int,input().split()))
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

functions = {
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b
             }

total_honey = 0

while nectar and bees:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        bees.appendleft(current_bee)
    else:
        total_honey += abs(functions[symbols.popleft()](current_bee, current_nectar))

print(f'Total honey made: {total_honey}')

if bees:
    print(f"Bees left: {', '.join(str(b) for b in bees)}")
if nectar:
    print(f"Nectar left: {' '.join(str(n) for n in nectar)}")
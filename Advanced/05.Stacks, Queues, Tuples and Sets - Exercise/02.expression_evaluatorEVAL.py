from collections import deque
from math import floor

expression = deque(input().split())

index = 0

while index < len(expression):

    element = expression[index]

    if element in "/*+-":
        for _ in range(index - 1):
            expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))

        del expression[1]
        index = 1

    index += 1

print(floor(int(expression[0])))

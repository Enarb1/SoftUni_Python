from functools import reduce
from math import floor

expressions = input().split()

index = 0
functions = {
    '*': lambda i: reduce(lambda a, b: a * b, map(int, expressions[:i])),
    '/': lambda i: reduce(lambda a, b: a / b, map(int, expressions[:i])),
    '+': lambda i: reduce(lambda a, b: a + b, map(int, expressions[:i])),
    '-': lambda i: reduce(lambda a, b: a - b, map(int, expressions[:i]))
}

while index < len(expressions):
    element = expressions[index]

    if element in "/*+-":
        expressions[0] = functions[element](index)
        [expressions.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(floor(int(expressions[0])))
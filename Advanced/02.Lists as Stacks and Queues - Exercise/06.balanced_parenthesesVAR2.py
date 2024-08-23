from collections import deque
"""This is my variant from Codewars"""
braces = deque(input())
opening_brackets = '([{'
closing_brackets = ')]}'
counter = 0
while braces and counter < len(braces) / 2:
    if braces[0] not in opening_brackets:
        break
    index = opening_brackets.index(braces[0])
    if braces[1] == closing_brackets[index]:
        braces.popleft()
        braces.popleft()
        braces.rotate(counter)
        counter = 0
    else:
        braces.rotate(-1)
        counter += 1

if braces:
    print('NO')
else:
    print('YES')
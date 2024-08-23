from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
secondary_colors = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for element in (first_word[:-1], second_word[:-1]):
            if element:
                words.insert(len(words) // 2, element)

for color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[color].issubset(result):
        result.remove(color)

print(result)

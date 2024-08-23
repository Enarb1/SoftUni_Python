word = input()
positions = []

for index, char in enumerate(word):
    if char.isupper():
        positions.append(index)
print(positions)



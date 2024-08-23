items_input = input().split()
dictionary = {}

for word in items_input:
    word_low = word.lower()
    if word_low not in dictionary:
        dictionary[word_low] = 0
    dictionary[word_low] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
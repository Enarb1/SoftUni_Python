count = int(input())
synonyms = {}
for word in range(count):
    main_word = input()
    synonym = input()
    if main_word not in synonyms.keys():
        synonyms[main_word] = []
    synonyms[main_word].append(synonym)

for word, synonym in synonyms.items():
    print(f'{word} - {", ".join(synonym)}')
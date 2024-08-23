results = {}
language_participants = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    submission = command.split("-")
    name = submission[0]
    if not 'banned' in submission:
        language = submission[1]
        points = int(submission[2])

        if name not in results.keys():
            results[name] = 0
        if points > results[name]:
            results[name] = points
        if language not in language_participants.keys():
            language_participants[language] = 0
        language_participants[language] += 1
    else:
        results.pop(name)

print("Results:")
for name, result in results.items():
    print(f'{name} | {result}')
print("Submissions:")
for lang, count in language_participants.items():
    print(f'{lang} - {count}')


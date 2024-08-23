import re

text = input()
pattern = r'(@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@)|(#[a-zA-Z]{3,}##[a-zA-Z]{3,}#)'
count = len(re.findall(pattern, text))
matches = re.finditer(pattern, text)
mirror_words = []

if count > 0:
    print(f'{count} word pairs found!')
else:
    print("No word pairs found!")
if matches:

    for match in matches:
        if match.group(1):
            words = match.group(1).replace('@', " ").strip().split()
            if words[0] == words[1][::-1]:
                mirror = f'{words[0]} <=> {words[1]}'
                mirror_words.append(mirror)
        elif match.group(2):
            words = match.group(2).replace('#', " ").strip().split()
            if words[0] == words[1][::-1]:
                mirror = f'{words[0]} <=> {words[1]}'
                mirror_words.append(mirror)

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(f'{", ".join(mirror_words)}')
else:
    print("No mirror words!")
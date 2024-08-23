import re

text = input()
coolness_threshold = 1
emojis = {}

for char in text:
    if char.isdigit():
        coolness_threshold *= int(char)

pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
emoji_count = len(re.findall(pattern,text))
matches = re.finditer(pattern, text)
print(f'Cool threshold: {coolness_threshold}')
print(f'{emoji_count} emojis found in the text. The cool ones are:')
for match in matches:
    emoji = match.group(0)
    emojis[emoji] = {'coolness': 0}
    coolness = sum(ord(char) for char in match.group(2))
    emojis[emoji]['coolness'] += coolness
    if emojis[emoji]['coolness'] >= coolness_threshold:
        print(emoji)

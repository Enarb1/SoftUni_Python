import re
text = input()
pattern = r'\b(?![._-])([a-zA-Z0-9_.-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z]+)([.a-zA-Z]+)?\b'
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0))
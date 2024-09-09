import re

with open("words.txt") as file:
    words = file.read()

words = words.split()

with open("text.txt") as file:
    text = file.read()

occ = {}
for word in words:

    pattern = rf'\b{word}\b'
    result = re.findall(pattern, text, re.IGNORECASE)
    #pattern = rf'\b{word}\b'
    occ[word] = len(result)

sorted_occ = sorted(occ.items(), key=lambda kvp: -kvp[1])

with open("output.txt", 'w') as file:
    for key, value in sorted_occ:
        file.write(f"{key} - {value}\n")



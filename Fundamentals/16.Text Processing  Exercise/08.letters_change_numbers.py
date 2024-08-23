import string
input_string = input().strip().split()
results = []

for word in input_string:
    num = int("".join([n for n in word if n.isdigit()]))
    total = 0
    if word[0].isupper():
        value = int(string.ascii_uppercase.index(word[0])) + 1
        total += (num / value)
    elif word[0].islower():
        value = int(string.ascii_lowercase.index(word[0])) + 1
        total += (num * value)
    if word[-1].isupper():
        value = int(string.ascii_uppercase.index(word[-1])) + 1
        total -= value
    elif word[-1].islower():
        value = int(string.ascii_lowercase.index(word[-1])) + 1
        total += value
    results.append(total)

print(f'{sum(results):.2f}')






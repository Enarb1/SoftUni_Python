text = input()
previous_char = ''
new_string = ''
for char in text:
    if char not in previous_char:
        new_string += char
    previous_char = char

print(new_string)



input_string = input()
encrypted = ''

for char in input_string:
    position = ord(char) + 3
    encrypted += chr(position)
print(encrypted)
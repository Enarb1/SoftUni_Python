def chars_in_range(a, b):
    characters = ""
    for chars in range(ord(a) + 1, ord(b)):
        characters += chr(chars) + " "

    return characters


char1 = input()
char2 = input()
print(chars_in_range(char1, char2))



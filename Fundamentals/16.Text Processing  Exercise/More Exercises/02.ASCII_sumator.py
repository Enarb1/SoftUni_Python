start = ord(input())
end = ord(input())
input_string = input()
characters = []

for char in input_string:
    if start < ord(char) < end:
        characters.append(ord(char))

print(sum(characters))




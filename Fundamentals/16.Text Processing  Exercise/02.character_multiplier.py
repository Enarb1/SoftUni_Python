string1, string2 = input().split()
total = 0
multiply_range = 0
to_add = ''
if len(string1) <= len(string2):
    multiply_range = len(string1)
    to_add = string2[multiply_range:]
else:
    multiply_range = len(string2)
    to_add = string1[multiply_range:]

for index in range(multiply_range):
    total += ord(string1[index]) * ord(string2[index])

for char in to_add:
    total += ord(char)
print(total)

keywords = int(input())
word = input()
list_strings = []

for index in range(keywords):
    current_string = input()
    list_strings.append(current_string)
print(list_strings)
for index in range(len(list_strings) -1, -1, -1):
    element = list_strings[index]
    if word not in element:
        list_strings.remove(element)
print(list_strings)
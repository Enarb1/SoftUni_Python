text = input()

paren_indexes =[]

for index in range(len(text)):
    if text[index] == '(':
        paren_indexes.append(index)
    elif text[index] == ')':
        start = paren_indexes.pop()
        end = index + 1
        print(text[start: end])
word = input()

while word != "End":
    if word != "SoftUni":
        new_word = ""
        for character in word:
            new_word += character * 2
        print(new_word)
    word = input()

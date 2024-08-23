c = 0
o = 0
n = 0

word = ""
while True:
    command = input()
    if command == "End":
        break
    else:
        letter = ord(command)
        if letter == 99 and c == 0:
            c += 1
            pass
        elif letter == 110 and n == 0:
            n += 1
            pass
        elif letter == 111 and o == 0:
            o += 1
            pass
        elif 64 < letter < 91 or 96 < letter < 123:
            word += chr(letter)
        if c == 1 and o == 1 and n == 1:
            print(word, end=" ")
            c = 0
            o = 0
            n = 0
            word = ""



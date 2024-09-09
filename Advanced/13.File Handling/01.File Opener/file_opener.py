try:
    file = open("text.txt", 'a+')
    print("File found")
    file.write('\nI am 35 years old.')
    file.seek(0)
    print(file.read())
except FileNotFoundError:
    print("File not found")

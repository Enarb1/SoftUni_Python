loop_range = int(input())

for _ in range(loop_range):
    text = input()
    name = text[text.index('@') + 1:text.index('|')]
    age = text[text.index('#') + 1:text.index('*')]
    print(f"{name} is {age} years old.")

lines = int(input())
balanced = 0
for index in range(lines):
    current_string = input()
    if current_string == "(":
        balanced += 1
        if balanced > 1:
            break
    elif current_string == ")":
        balanced -= 1
        if balanced < 1:
            break
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")

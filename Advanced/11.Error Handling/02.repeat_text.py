text = input()

try:
    multiplier = int(input())

except ValueError:
    print("Variable times must be an integer")

else:
    result = text * multiplier
    print(result)

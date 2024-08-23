rows = int(input())

width = rows
for i in range(1, (width + 1) // 2 + 1):
    print(" " * (width // 2 - i + 1), end="")
    print("*" * (2 * i - 1))
for i in range((width - 1) // 2, 0, -1):
    print(" " * (width // 2 - i + 1), end="")
    print("*" * (2 * i - 1))

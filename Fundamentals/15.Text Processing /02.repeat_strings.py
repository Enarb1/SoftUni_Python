strings = input().split()
result = "".join(word * len(word) for word in strings)
print(result)
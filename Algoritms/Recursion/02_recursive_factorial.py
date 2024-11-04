def factorial(n, idx=0):
    if n == 1:
        return n
    return n * factorial(n - 1, idx + 1)


number = int(input())
print(factorial(number))
def recursive_factorial(n):
    if n == 1:
        return n

    return n * recursive_factorial(n - 1)


number = int(input())
print(recursive_factorial(number))
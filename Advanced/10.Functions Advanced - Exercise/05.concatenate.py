def concatenate(*args, **kwargs):
    result = ''.join(args)

    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
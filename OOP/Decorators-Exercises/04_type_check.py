def type_check (param):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, param):
                    return "Bad Type"

            return func(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
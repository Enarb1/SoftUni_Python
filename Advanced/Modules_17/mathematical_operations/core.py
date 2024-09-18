def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")


def multiplication(a, b):
    return a * b


def subtract(a, b):
    return a - b


def add_nums(a, b):
    return a + b


def rais_nums(a, b):
    return a ** b


mapper = {
    "/": divide,
    "*": multiplication,
    "-": subtract,
    "+": add_nums,
    "^": rais_nums
}

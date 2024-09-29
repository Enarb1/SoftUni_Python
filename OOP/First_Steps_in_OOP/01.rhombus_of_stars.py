n = int(input())


def console_print(size, row):
    print(" " * (size - row) + "* " * row)


def upper_part(size):
    for row in range(1, size + 1):
        console_print(size, row)


def lower_part(size):
    for row in range(size - 1, 0, -1):
        console_print(size, row)


def build_rhombus(size):
    upper_part(size)
    lower_part(size)

build_rhombus(n)

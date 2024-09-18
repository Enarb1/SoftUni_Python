def upper_part(num):
    for row_n in range(1, num + 1):
        for n in range(1, row_n + 1):
            print(n, end=' ')
        print()


def bottom_part(num):
    for row_n in range(1, num):
        for n in range(1, num - row_n + 1):
            print(n, end=' ')
        print()


def print_triangle(num):
    upper_part(num)
    bottom_part(num)



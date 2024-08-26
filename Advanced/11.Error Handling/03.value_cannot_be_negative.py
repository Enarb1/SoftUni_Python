class ValueCannotBeNegative(Exception):
    pass


for i in range(5):
    n = int(input())
    if n < 0:
        raise ValueCannotBeNegative
import math

def distance_from_center(x, y):
    return math.sqrt(x**2 + y**2)

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def print_closest_point_first(x1, y1, x2, y2):
    if distance_from_center(x1, y1) <= distance_from_center(x2, y2):
        return (x1, y1, x2, y2)
    else:
        return (x2, y2, x1, y1)

def print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length1 = line_length(x1, y1, x2, y2)
    length2 = line_length(x3, y3, x4, y4)

    if length1 >= length2:
        p1, p2, p3, p4 = print_closest_point_first(x1, y1, x2, y2)
    else:
        p1, p2, p3, p4 = print_closest_point_first(x3, y3, x4, y4)

    print(f"({math.floor(p1)}, {math.floor(p2)})({math.floor(p3)}, {math.floor(p4)})")

# Example usage:
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4)

import math

def distance_from_center(x, y):
    return math.sqrt(x**2 + y**2)

def print_closest_point(x1, y1, x2, y2):
    distance1 = distance_from_center(x1, y1)
    distance2 = distance_from_center(x2, y2)

    if distance1 <= distance2:
        closest_x = math.floor(x1)
        closest_y = math.floor(y1)
    else:
        closest_x = math.floor(x2)
        closest_y = math.floor(y2)

    print(f"({closest_x}, {closest_y})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print_closest_point(x1, y1, x2, y2)

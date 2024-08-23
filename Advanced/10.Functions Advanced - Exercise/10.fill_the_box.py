from collections import deque


def fill_the_box(height, length, width, *cubes):
    box_space = height * length * width
    cubes = deque(cubes)

    while cubes[0] != "Finish":

        box_space -= cubes.popleft()

        if box_space < 0:
            cubes_left = sum(el for el in cubes if el != 'Finish')
            return f"No more free space! You have {cubes_left + abs(box_space)} more cubes."

    return f"There is free space in the box. You could put {box_space} more cubes."



print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

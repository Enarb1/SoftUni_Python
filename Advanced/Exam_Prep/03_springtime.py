def start_spring(**objects):

    spring = {}

    for obj, _type in sorted(objects.items()):
        spring[_type] = spring.get(_type,[]) + [obj]

    sorted_spring = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))
    message = ""

    for object_type, objs in sorted_spring:
        message += f"{object_type}:\n"
        message += '\n'.join(f"-{o}" for o in objs) + "\n"

    return message


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
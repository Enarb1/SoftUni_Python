students_dict = {}
command = input()

while ":" in command:
    info = command.split(":")
    name, id_, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id_] = name
    command = input()

course = " ".join(command.split("_"))

for key, value in students_dict.items():
    if key == course:
        for id_, name in value.items():
            print(f"{name} - {id_}")





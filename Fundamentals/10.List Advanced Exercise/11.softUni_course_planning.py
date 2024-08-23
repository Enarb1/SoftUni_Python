def add_lesson(lessons_list, lesson):
    if lesson not in lessons_list:
        lessons_list.append(lesson)


def insert_lesson(lessons_list, lesson, index):
    if lesson not in lessons_list:
        lessons_list.insert(index, lesson)


def remove_lesson(lessons_list, lesson):
    if lesson in lessons_list:
        lessons_list.remove(lesson)
        exercise = lesson + "-Exercise"
        if exercise in lessons_list:
            lessons_list.remove(exercise)


def swap_lessons(lessons_list, lesson_one, lesson_two):
    if lesson_one in lessons_list and lesson_two in lessons_list:
        index_one, index_two = lessons_list.index(lesson_one), lessons_list.index(lesson_two)

        lessons_list[index_one], lessons_list[index_two] = lessons_list[index_two], lessons_list[index_one]

        exercise_one, exercise_two = lesson_one + "-Exercise", lesson_two + "-Exercise"

        if exercise_one in lessons_list:
            lessons_list.remove(exercise_one)
            lessons_list.insert(lessons_list.index(lesson_one) + 1, exercise_one)

        if exercise_two in lessons_list:
            lessons_list.remove(exercise_two)
            lessons_list.insert(lessons_list.index(lesson_two) + 1, exercise_two)


def exercise_task(lessons_list, exercise, lesson):
    exercise_title = lesson + "-Exercise"
    if lesson in lessons_list:
        lesson_index = lessons_list.index(lesson)
        if exercise_title not in lessons_list:
            lessons_list.insert(lesson_index + 1, exercise_title)
    else:
        lessons_list.append(lesson)
        lessons_list.append(exercise_title)


def process_commands(lessons_list, commands):

    for command in commands:
        command_parts = command.split(":")

        if command_parts[0] == "Add":
            lesson = command_parts[1]
            add_lesson(lessons_list, lesson)
        elif command_parts[0] == "Insert":
            lesson = command_parts[1]
            index = int(command_parts[2])
            insert_lesson(lessons_list, lesson, index)
        elif command_parts[0] == "Remove":
            lesson = command_parts[1]
            remove_lesson(lessons_list, lesson)
        elif command_parts[0] == "Swap":
            lesson_one = command_parts[1]
            lesson_two = command_parts[2]
            swap_lessons(lessons_list, lesson_one, lesson_two)
        elif command_parts[0] == "Exercise":
            exercise = command_parts[1]
            lesson = command_parts[1]
            exercise_task(lessons_list, exercise, lesson)

    return lessons_list


lessons = input().split(", ")
commands = []

while True:
    command = input()
    if command == "course start":
        break
    commands.append(command)

final_schedule = process_commands(lessons, commands)
for index, lesson_type in enumerate(final_schedule, 1):
    print(f"{index}.{lesson_type}")
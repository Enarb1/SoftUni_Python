negative_grade_max = int(input())
tasks = 0
failed = 0
total_score = 0
last_task_name = ""

while True:
    command = input()
    if command == "Enough":
        print(f"Average score: {total_score / tasks:.2f}")
        print(f"Number of problems: {tasks}")
        print(f"Last problem: {last_task_name}")
        break
    else:
        score = int(input())
        last_task_name = ""
        last_task_name += command

        if score <= 4:
            failed += 1
            if failed == negative_grade_max:
                print(f"You need a break, {failed} poor grades.")
                break
        tasks += 1
        total_score += score






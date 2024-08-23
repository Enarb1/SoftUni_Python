juri = int(input())
total_number = 0
total_scores = 0

while True:
    command = input()
    if command == "Finish":
        print(f"Student's final assessment is {total_scores / total_number:.2f}.")
        break
    else:
        presentation = ''
        presentation = command
        sum_score = 0

        for i in range(juri):
            score = float(input())
            sum_score += score
            total_scores += score
            total_number += 1

    print(f"{presentation} - {sum_score / juri:.2f}.")


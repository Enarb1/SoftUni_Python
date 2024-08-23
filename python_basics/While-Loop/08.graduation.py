student_name = input()

years_counter = 0
failed_years = 0
total_grades = 0

while years_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years +=1
        if failed_years == 2:
            print(f"{student_name} has been excluded at {years_counter + 1} grade")
            break

        continue

    total_grades += annual_grade
    years_counter += 1
else:

    print(f"{student_name} graduated. Average grade: {total_grades / years_counter:.2f}")


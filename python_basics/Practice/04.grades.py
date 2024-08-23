students = int(input())
total_grades = 0
failed = 0
between3_and_399 = 0
between4_and_499 = 0
top_students = 0


for _ in range(1, students + 1):
    grade = float(input())
    total_grades += grade
    if grade < 3:
        failed += 1
    if 3 <= grade < 4:
        between3_and_399 += 1
    if 4 <= grade < 5:
        between4_and_499 += 1
    if grade >= 5:
        top_students += 1
print(f"Top students: {top_students / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between4_and_499 / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between3_and_399 / students * 100:.2f}%")
print(f"Fail: {failed / students * 100:.2f}%")
print(f"Average: {total_grades / students:.2f}")

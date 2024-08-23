employee1_per_h = int(input())
employee2_per_h = int(input())
employee3_per_h = int(input())
total_students = int(input())

students_per_h = employee1_per_h + employee2_per_h + employee3_per_h
hour = 0
if total_students ==0:
    print(f"Time needed: {hour}h.")
else:
    while total_students:
        hour += 1
        if hour % 4 == 0:
            total_students -= 0
        else:
            total_students -= students_per_h
        if total_students <= 0:
            hours_needed = hour
            print(f"Time needed: {hours_needed}h.")
            break


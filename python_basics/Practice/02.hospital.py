treated_patients = 0
untreated_patients = 0
doctors = 7
day = 0

for _ in range(1, int(input()) + 1):
    patients = int(input())
    day += 1
    if day == 3:
        if untreated_patients > treated_patients:
            doctors += 1
        day = 0
    if doctors >= patients:
        treated_patients += patients
    else:
        untreated = abs(doctors - patients)
        untreated_patients += untreated
        treated_patients += doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
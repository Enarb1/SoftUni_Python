def age_assignment(*names, **ages):
    names = sorted(names)

    result = []

    for name in names:
        age = ages[name[0]]
        result.append(f"{name} is {age} years old.")

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
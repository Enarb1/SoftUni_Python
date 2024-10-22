def list_roman_emperors(*emperors,**rule_length):
    successful = {}
    unsuccessful = {}

    for emperor, success in emperors:
        if success:
            successful[emperor] = 0
        else:
            unsuccessful[emperor] = 0

    for name, years in rule_length.items():
        if name in successful.keys():
            successful[name] += years
        else:
            unsuccessful[name] += years


    successful_sorted = sorted(successful.items(), key=lambda x: (-x[1],x[0]))
    unsuccessful_sorted = sorted(unsuccessful.items(), key=lambda x: (x[1],x[0]))

    message = f"Total number of emperors: {len(emperors)}\n"
    if successful_sorted:
        message += "Successful emperors:\n"
        message += '\n'.join(f"****{name}: {years}" for name, years in successful_sorted) + "\n"
    if unsuccessful_sorted:
        message += "Unsuccessful emperors:\n"
        message += '\n'.join(f"****{name}: {years}" for name, years in unsuccessful_sorted) + "\n"

    return message


# print(list_roman_emperors(("Augustus", True), ("Trajan", True),
#                           ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True),
#                           Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))

# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
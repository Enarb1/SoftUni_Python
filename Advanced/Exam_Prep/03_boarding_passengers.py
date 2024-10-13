def boarding_passengers(initial_capacity,*passenger_groups ):
    boarded = {}
    capacity = initial_capacity


    for count, program in passenger_groups:
        if capacity == 0:
            break
        if count <=capacity:
            capacity -= count
            boarded[program] = boarded.get(program, 0) + count


    passengers_sorted = sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    total_passengers = sum(n for n, p in passenger_groups)
    boarded_passengers = sum(boarded.values())

    message = "Boarding details by benefit plan:\n"
    message += '\n'.join(f"## {plan}: {number} guests" for plan, number in passengers_sorted)

    if total_passengers == boarded_passengers:
        message += "\nAll passengers are successfully boarded!"
    elif capacity == 0:
        message += "\nBoarding unsuccessful. Cruise ship at full capacity."
    else:
        message += f"\nPartial boarding completed. Available capacity: {capacity}."

    return message

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
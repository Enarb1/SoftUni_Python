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
    for plan, number in passengers_sorted:
        message += f"## {plan}: {number} guests\n"

    if total_passengers == boarded_passengers:
        message += "All passengers are successfully boarded!"
    elif capacity == 0:
        message += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        message += f"Partial boarding completed. Available capacity: {capacity}."

    return message

print(boarding_passengers(5, (10, 'Diamond'), (20, 'Platinum'),
                          (10, 'Gold'), (20, 'First Cruiser'), (10, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
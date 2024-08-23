def revert_func(cars, car, kilometers):
    min_km = 10_000
    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] < min_km:
        cars[car]['mileage'] = min_km
    else:
        print(f'{car} mileage decreased by {kilometers} kilometers')
    return cars


def refuel_func(cars, car, fuel):
    max_liter = 75
    if cars[car]['fuel'] + fuel > max_liter:
        fuel = max_liter - cars[car]['fuel']
    cars[car]['fuel'] += fuel
    print(f'{car} refueled with {fuel} liters')

    return cars


def drive_func(cars, car, distance, fuel):
    max_km = 100_000
    if cars[car]['fuel'] >= fuel:
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]['mileage'] >= max_km:
            print(f'Time to sell the {car}!')
            del cars[car]
    else:
        print(f'Not enough fuel to make that ride')
    return cars


def process_commands(cars):
    while True:
        command = input()
        if command == 'Stop':
            break
        info = command.split(' : ')
        action = info[0]
        car = info[1]
        if action == 'Drive':
            distance = int(info[2])
            fuel = int(info[3])
            cars = drive_func(cars, car, distance, fuel)
        elif action == 'Refuel':
            fuel = int(info[2])
            cars = refuel_func(cars, car, fuel)
        elif action == 'Revert':
            kilometers = int(info[2])
            cars = revert_func(cars, car, kilometers)

    for car in cars.keys():
        mileage = cars[car]['mileage']
        fuel = cars[car]['fuel']
        print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def add_cars(loop_range):
    cars = {}
    for _ in range(loop_range):
        car, (mileage), fuel = input().split('|')
        if car not in cars.keys():
            cars[car] = {'mileage': 0, 'fuel': 0}
        cars[car]['mileage'] += int(mileage)
        cars[car]['fuel'] += int(fuel)
    return cars


loop_r = int(input())
cars_dict = add_cars(loop_r)
process_commands(cars_dict)

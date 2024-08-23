def drive(cars, car, distance, fuel, MAX_KM):

    if cars[car]['fuel'] >= fuel:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]['mileage'] >= MAX_KM:
            print(f'Time to sell the {car}!')
            del cars[car]

    else:
        print('Not enough fuel to make that ride')

    return cars


def refuel(cars, car, fuel, MAX_FUEL):

    if cars[car]['fuel'] + fuel > MAX_FUEL:
        refueled_for = MAX_FUEL - cars[car]['fuel']
    else:
        refueled_for = fuel
    cars[car]['fuel'] += fuel
    if cars[car]['fuel'] > MAX_FUEL:
        cars[car]['fuel'] = MAX_FUEL
    print(f'{car} refueled with {refueled_for} liters')

    return cars


def revert_km(cars, car, kilometers, MIN_KM):

    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] > MIN_KM:
        print(f'{car} mileage decreased by {kilometers} kilometers')
    else:
        cars[car]['mileage'] = MIN_KM

    return cars


def process_commands(cars):
    MAX_KM = 100000
    MIN_KM = 10000
    MAX_FUEL = 75

    while True:
        command = input()
        if command == 'Stop':
            break
        info = command.split(" : ")
        action = info[0]
        car = info[1]
        if action == 'Drive':
            distance = int(info[2])
            fuel = int(info[3])
            cars = drive(cars, car, distance, fuel, MAX_KM)
        elif action == 'Refuel':
            fuel = int(info[2])
            cars = refuel(cars, car, fuel, MAX_FUEL)
        elif action == 'Revert':
            kilometers = int(info[2])
            cars = revert_km(cars, car, kilometers, MIN_KM)

    for car in cars.keys():
        mileage = cars[car]['mileage']
        fuel = cars[car]['fuel']
        print(f'{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def add_cars(loop_range, cars):

    for _ in range(loop_range):
        car, mileage, fuel = input().split("|")
        if car not in cars.keys():
            cars[car] = {}
        cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

    return cars


loop_n = int(input())
cars_lst = {}
cars_lst = add_cars(loop_n, cars_lst)
process_commands(cars_lst)



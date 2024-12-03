from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race

class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CAR_TYPES.keys():
            if self.__get_car_by_model(model) is not None:
                raise Exception(f"Car {model} is already created!")
            car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {car.model} is created."

    def create_driver(self, driver_name: str):
        if self.__get_driver_by_name(driver_name) is not None:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver.name} is created."

    def create_race(self, race_name: str):
        if self.__get_race_by_name(race_name) is not None:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race.name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)
        car = self.__get_car_by_type(car_type)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if car is None or car.is_taken:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car is not None:
            old_car = driver.car
            old_car.is_taken = False
            car.is_taken = True
            driver.car = car
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."
        car.is_taken = True
        driver.car = car
        return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)
        driver= self.__get_driver_by_name(driver_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver.name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver.name} added in {race.name} race."

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        sorted_drivers_in_race = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        winners = sorted_drivers_in_race[:3]
        result = []
        for d in winners:
            d.number_of_wins += 1
            result.append(f"Driver {d.name} wins the {race.name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(result)

    def __get_car_by_type(self, car_type):
        for i in range(len(self.cars) -1, -1, -1):
            if type(self.cars[i]).__name__ == car_type and not self.cars[i].is_taken:
                return self.cars[i]
        return None

    def __get_race_by_name(self, race_name):
        return next((r for r in self.races if r.name == race_name), None)

    def __get_driver_by_name(self, driver_name):
        return next((d for d in self.drivers if d.name == driver_name), None)

    def __get_car_by_model(self, model):
        return next((c for c in self.cars if c.model == model), None)

from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    LOAD_BATTERY_REDUCE = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_battery = mileage / self.MAX_MILEAGE * 100 + self.LOAD_BATTERY_REDUCE
        self.battery_level -= reduce_battery
        self.battery_level = round(self.battery_level)
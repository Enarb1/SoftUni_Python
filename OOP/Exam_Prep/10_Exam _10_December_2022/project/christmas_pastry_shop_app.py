from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth



class ChristmasPastryShopApp:

    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }


    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0


    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        if self.__get_delicacy(name) is not None:
            raise Exception(f"{name} already exists!")

        try:
            delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        except KeyError:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {delicacy.__class__.__name__} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__get_booth(booth_number) is not None:
            raise Exception(f"Booth number {booth_number} already exists!")

        try:
            booth = self.VALID_BOOTS[type_booth](booth_number, capacity)
        except KeyError:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth)
        return f"Added booth number {booth.booth_number} in the pastry shop."


    def reserve_booth(self, number_of_people: int) -> str:
        booth = next((b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved), None)
        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."


    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = self.__get_booth(booth_number)
        delicacy = self.__get_delicacy(delicacy_name)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy.name}."


    def leave_booth(self, booth_number: int) -> str:
        booth = self.__get_booth(booth_number)
        bill = booth.get_bill()
        self.income+= bill

        return f"""Booth {booth.booth_number}:
Bill: {bill:.2f}lv."""


    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."


    def __get_booth(self, number):
        return next((b for b in self.booths if b.booth_number == number), None)


    def __get_delicacy(self, name):
        return next((d for d in self.delicacies if d.name == name), None)

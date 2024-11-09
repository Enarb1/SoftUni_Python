from abc import ABC, abstractmethod

class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: list = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")

        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        ...


    def get_total_equipment_price(self):
        return sum([e.price for e in self.equipment])


    def get_average_protection(self):
        try:
            avg_protection = int(sum(e.protection for e in self.equipment) / len(self.equipment))
        except ZeroDivisionError:
            return 0

        return avg_protection


    def get_statistics(self):  #possible to have to add a new line after the last row
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {self.get_total_equipment_price():.2f}\n"
                f"Average Protection: {self.get_average_protection()}")

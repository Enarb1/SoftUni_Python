from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list = []
        self.competition_points: float = 0.0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")

        self.__name = value

    @property
    def oxygen_level(self):
        return self._oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0 :
            raise ValueError("Cannot create diver with negative oxygen level!")

        self._oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
        else:
            self.catch.append(fish)
            self.competition_points += fish.points
            self.oxygen_level -= fish.time_to_catch

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"[Name: {self.name}, "
                f"Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]")

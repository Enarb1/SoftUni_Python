from abc import ABC, abstractmethod


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @abstractmethod
    def increase_money(self):
        ...

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        return self.available_money >= artifact_price  and self.available_space >= artifact_space_required

    def __str__(self):
        sorted_artifacts = sorted(self.purchased_artifacts, key=lambda a: a.name, reverse=True)
        artifacts = ", ".join(a.name for a in sorted_artifacts) if sorted_artifacts else "none"
        return (f"Collector name: {self.name}; "
                f"Money available: {self.available_money:.2f}; "
                f"Space available: {self.available_space};"
                f" Artifacts: {artifacts}")

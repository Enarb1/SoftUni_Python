from abc import ABC


class Car(ABC):
    MIN_SPEED = None
    MAX_SPEED = None

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value): #possible min speed limit exclusive
        if not self.MIN_SPEED <= value <= self.MAX_SPEED:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED} and {self.MAX_SPEED}!")
        self.__speed_limit = value
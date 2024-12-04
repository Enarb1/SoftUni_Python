from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90
    BREATH = 15

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)

    def breathe(self):
        self.oxygen -= self.BREATH
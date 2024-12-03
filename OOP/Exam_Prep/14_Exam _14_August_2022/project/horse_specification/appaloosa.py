from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_HORSE_SPEED = 120
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed):
        super().__init__(name, speed)


    def train(self):
        if self.speed + self.SPEED_INCREASE <= self.MAX_HORSE_SPEED:
            self.speed += self.SPEED_INCREASE
        else:
            self.speed = self.MAX_HORSE_SPEED
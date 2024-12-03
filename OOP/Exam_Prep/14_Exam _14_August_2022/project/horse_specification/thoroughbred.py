from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_HORSE_SPEED = 140
    SPEED_INCREASE = 3

    def __init__(self, name: str, speed):
        super().__init__(name, speed)


    def train(self):
        if self.speed + self.SPEED_INCREASE <= self.MAX_HORSE_SPEED:
            self.speed += self.SPEED_INCREASE
        else:
            self.speed = self.MAX_HORSE_SPEED
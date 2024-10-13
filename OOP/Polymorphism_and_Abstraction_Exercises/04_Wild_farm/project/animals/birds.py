from project.animals.animal import Bird
from project.food import Fruit, Vegetable, Meat, Seed


class Owl(Bird):
    @property
    def gain_weight(self):
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def gain_weight(self):
        return 0.35

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @staticmethod
    def make_sound():
        return "Cluck"


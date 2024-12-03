from project.supply.supply import Supply


class Food(Supply):
    INITIAL_ENERGY = 25

    def __init__(self, name, energy=INITIAL_ENERGY):
        super(Food, self).__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
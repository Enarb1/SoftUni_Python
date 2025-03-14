from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INITIAL_SIZE = 3
    AQUARIUM = "FreshwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    def eat(self):
        self.size += 3
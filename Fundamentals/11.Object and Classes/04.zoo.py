class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fishes.append(animal)
        elif species == 'bird':
            self.birds.append(animal)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            mammals_print = ", ".join(self.mammals)
            result += f"Mammals in {self.name}: {mammals_print}\n"
        elif species == "fish":
            fishes_print = ", ".join(self.fishes)
            result += f"Fishes in {self.name}: {fishes_print}\n"
        elif species == "bird":
            birds_print = ", ".join(self.birds)
            result += f"Birds in {self.name}: {birds_print}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
animals_count = int(input())

for animal_type in range(animals_count):
    animal_input = input().split()
    species = animal_input[0]
    animal = animal_input[1]
    zoo.add_animal(species, animal)

info = input()

print(zoo.get_info(info))

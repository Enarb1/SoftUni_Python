from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    VALID_DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    VALID_FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        try:
            aquarium = self.VALID_AQUARIUM_TYPES[aquarium_type](aquarium_name)
        except KeyError:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        try:
            decoration = self.VALID_DECORATION_TYPES[decoration_type]()
        except KeyError:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium is not None and decoration is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration.__class__.__name__} to {aquarium.name}."
        if aquarium is not None and decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)
        except KeyError:
            return f"There isn't a fish of type {fish_type}."
        if aquarium is not None:
            if fish.AQUARIUM != aquarium.__class__.__name__:
                return "Water not suitable."
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            total_value = sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decorations)
            return f"The value of Aquarium {aquarium.name} is {total_value:.2f}."

    def report(self):
        result = []
        for a in self.aquariums:
            result.append(str(a))
        return "\n".join(result)

    def __get_aquarium_by_name(self, name):
        return next((a for a in self.aquariums if a.name == name), None)

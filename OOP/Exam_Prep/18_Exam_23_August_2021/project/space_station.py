from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."
        try:
            astronaut = self.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        except KeyError:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items.extend(items.split(", "))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        amount = 10
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(amount)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")
        astronauts = self.__pick_astronauts()

        participating_astronauts = 0

        for a in astronauts:
            participating_astronauts += 1

            while planet.items and a.oxygen > 0:
                item = planet.items.pop()
                a.backpack.append(item)
                a.breathe()

            if not planet.items:
                self.successful_missions += 1
                return (f"Planet: {planet.name} was explored. {participating_astronauts} "
                        f"astronauts participated in collecting items.")
        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [
            f"{self.successful_missions} successful missions!",
            f"{self.unsuccessful_missions} missions were not completed!",
            "Astronauts' info:"
        ]

        for a in self.astronaut_repository.astronauts:
            back_pack_items = ', '.join(a.backpack) if a.backpack else "none"
            result.extend([f"Name: {a.name}", f"Oxygen: {a.oxygen}", f"Backpack items: {back_pack_items}"])

        return "\n".join(result)

    def __pick_astronauts(self):
        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable_astronauts.sort(key=lambda a: a.oxygen, reverse=True)

        return suitable_astronauts[:5]

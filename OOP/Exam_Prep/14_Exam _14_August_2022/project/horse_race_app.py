from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace

class HorseRaceApp:

    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []
        self.race_types_created :list = []


    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = next((h for h in self.horses if h.name == horse_name), None)
        if horse is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in self.VALID_HORSE_TYPES.keys():
            horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):
        jockey = self.__get_jockey(jockey_name)
        if jockey is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."


    def create_horse_race(self, race_type: str):
        if race_type in self.race_types_created:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        self.race_types_created.append(race.race_type)
        return f"Race {race.race_type} is created."


    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = next((h for h in reversed(self.horses) if h.__class__.__name__ == horse_type and not h.is_taken),None)
        jockey = self.__get_jockey(jockey_name)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!") #TODO try to put it in a function
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f"Jockey {jockey.name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey.name} will ride the horse {horse.name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__get_jockey(jockey_name)
        horse_race = next((r for r in self.horse_races if r.race_type == race_type), None)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey.name} cannot race without a horse!")
        if self.__is_jockey_already_added_in_race(jockey.name,horse_race) is not None:
            return f"Jockey {jockey.name} has been already added to the {horse_race.race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey.name} added to the {horse_race.race_type} race."


    def start_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race.race_type} needs at least two participants!")

        winner = max(race.jockeys, key=lambda j: j.horse.speed)
        winner_horse = winner.horse
        return (f"The winner of the {race.race_type} race, with a speed of {winner_horse.speed}km/h is {winner.name}! "
                f"Winner's horse: {winner_horse.name}.")


    def __is_jockey_already_added_in_race(self, jockey_name: str, horse_race):
        return next((j for j in horse_race.jockeys if j.name == jockey_name), None)

    def __get_jockey(self, name):
        return next((j for j in self.jockeys if j.name == name), None)

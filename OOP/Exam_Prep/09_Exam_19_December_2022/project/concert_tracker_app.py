from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band import Band
from project.concert import Concert

class ConcertTrackerApp:

    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }


    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []


    def create_musician(self, musician_type: str, name: str, age: int):
        try:
            musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        except KeyError:
            raise ValueError("Invalid musician type!")

        if self.__get_musician(musician.name) is not None:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."


    def create_band(self, name: str):
        if self.__get_band(name) is not None:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        check_concert = self.__get_concert(place)

        if check_concert is not None:
            raise Exception(f"{place} is already registered for {check_concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."


    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__get_musician(musician_name)
        band = self.__get_band(band_name)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."


    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__get_band(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band_member = next((m for m in band.members if m.name == musician_name), None)
        if band_member is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(band_member)

        return f"{musician_name} was removed from {band_name}."


    def start_concert(self, concert_place: str, band_name: str):
        band = self.__get_band(band_name)
        concert = self.__get_concert(concert_place)
        required_skills = {
            "Rock": ConcertTrackerApp.__rock_concert_req_skills,
            "Metal": ConcertTrackerApp.__metal_concert_req_skills,
            "Jazz": ConcertTrackerApp.__jazz_concert_req_skills,
        }

        if not self.__has_all_musician_types(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        req_skills = required_skills[concert.genre]()
        for member in band.members:
            member_type = member.__class__.__name__
            for skill in req_skills[member_type]:
                if skill not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        else:
           profit = (concert.audience * concert.ticket_price) - concert.expenses


        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."


    @staticmethod
    def __jazz_concert_req_skills():
        return {
            "Drummer": ["play the drums with drum brushes"],
            "Singer": ["sing high pitch notes", "sing low pitch notes"],
            "Guitarist": ["play jazz"]
        }
    @staticmethod
    def __metal_concert_req_skills():
        return {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing low pitch notes"],
            "Guitarist": ["play metal"]
        }

    @staticmethod
    def __rock_concert_req_skills():
        return {
            "Drummer": ["play the drums with drumsticks"],
            "Singer": ["sing high pitch notes"],
            "Guitarist": ["play rock"]
        }

    def __has_all_musician_types(self, band):
        required_types = {Drummer, Guitarist, Singer}
        return all(any(isinstance(m, req_type) for m in band.members) for req_type in required_types)

    def __get_concert(self, place: str):
        return next((c for c in self.concerts if c.place == place), None)


    def __get_band(self, name: str):
        return next((b for b in self.bands if b.name == name), None)


    def __get_musician(self, name:str):
        return next((m for m in self.musicians if m.name == name), None)
